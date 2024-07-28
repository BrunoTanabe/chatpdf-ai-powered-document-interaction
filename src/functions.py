# functions.py: Script para criar as funções necessárias para o ChatPDF

## IMPORTAÇÃO DOS PACOTES NECESSÁRIOS

### Pacotes Locais
from models import llama3_model
### Pacotes do Python
import os
from PyPDF2 import PdfReader
from dotenv import load_dotenv
### Pacotes do LangChain
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain, create_history_aware_retriever

## FUNÇÕES

### Função para extrair o conteúdo de um documento PDF
def get_pdf_content(documents):
    raw_text = ""

    for document in documents:
        pdf_reader = PdfReader(document)
        for page in pdf_reader.pages:
            raw_text += page.extract_text()

    return raw_text

### Função para dividir o texto em pedaços menores
def get_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    text_chunks = text_splitter.split_text(text)
    
    return text_chunks

### Função para criar um vetor de embeddings a partir dos pedaços de texto
def get_vectorstore(chunks):
    embeddings = HuggingFaceEmbeddings()
    vectorstore = FAISS.from_texts(texts=chunks, embedding=embeddings)

    return vectorstore

### Função para encadear a conversa com o chatbot
def conversation_chain(user_message, vectorstore, chat_history):
   
    chat_llm = llama3_model
    retriever = vectorstore.as_retriever()
    
    contextualize_q_system_prompt = (
        "Given a chat history and the latest user question "
        "which might reference context in the chat history, "
        "formulate a standalone question which can be understood "
        "without the chat history. Do NOT answer the question, "
        "just reformulate it if needed and otherwise return it as is."
    )
    
    contextualize_q_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", contextualize_q_system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )
    
    history_aware_retriever = create_history_aware_retriever(
        chat_llm, retriever, contextualize_q_prompt
    )
    
    system_prompt = (
        "You are Doc, an friendly assistant for question-answering tasks."
        "Use the following pieces of retrieved context to answer their "
        "questions accurately and clearly. Always offer additional tips to enhance "
        "their experience. Always respond using best markdown (.md) formatting practices and emojis."
        "If any information is not specified in the document, inform the user that you do not have this information in the documents."
        "\n\n"
        "{context}"
    )
    
    qa_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )
    
    question_answer_chain = create_stuff_documents_chain(chat_llm, qa_prompt)
    rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)
    
    # response = rag_chain.invoke({"input": user_message, "chat_history": chat_history})
    # return response["answer"]
    
    for chunk in rag_chain.stream({"input": user_message, "chat_history": chat_history}):   
        if answer_chunk := chunk.get("answer"):
            yield answer_chunk
            
    return
    