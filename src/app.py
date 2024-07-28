# app.py: Script para criar a interface do ChatPDF

## IMPORTAÇÃO DOS PACOTES NECESSÁRIOS
### Pacotes Locais
from functions import get_pdf_content, get_chunks, get_vectorstore, conversation_chain
from html_template import css, ai_template, human_template, hide_st_style
### Pacotes Streamlit
import streamlit as st
### Pacotes do LangChain
from langchain.schema import HumanMessage, AIMessage

## FUNÇÕES

### Função para gerar a página do chatbot
def generate_page():
    st.set_page_config(page_title="ChatPDF",
        page_icon="./src/assets/favicon.ico", 
        layout="wide",
        initial_sidebar_state="expanded",
    )
    
    st.write(css, unsafe_allow_html=True)
    st.markdown(hide_st_style, unsafe_allow_html=True)
    
    with st.sidebar:
        st.image("./src/assets/vertical_logo.png", use_column_width=True)
        st.subheader("", divider="red")
        st.subheader("")
        
        if uploaded_files := st.file_uploader(label="Upload your PDFs files here and click on 'PROCESS'", type=["pdf"], accept_multiple_files=True, help="Insert your PDF documents that you want to chat with them."):
            if st.button(label="PROCESS", help="Click here to process the uploaded PDF files.", use_container_width=True):
                with st.status(label="Processing PDFs files", expanded=False):
                    st.write("Pre-processing PDFs files...")
                    if "vectorstore" in st.session_state:
                        del st.session_state["vectorstore"]
                    
                    if "chat_history" in st.session_state:
                        del st.session_state["chat_history"]
                        
                    st.session_state["files_names"] = ""
                    for file in uploaded_files:
                        st.session_state["files_names"] += file.name + ", "
                    
                    st.write("Get PDF Text...")
                    raw_text = get_pdf_content(uploaded_files)
                    
                    st.write("Get Text Chunks...")
                    text_chunks = get_chunks(raw_text)
                    
                    st.write("Create VectorStore...")
                    st.session_state['vectorstore'] = get_vectorstore(text_chunks)
                    
                    # st.write("Create Conversation Chain...")
                    # conversation = conversation_chain(vectorstore)
    
        if st.button(label="NEW CHAT", use_container_width=True):
            if "chat_history" in st.session_state:  
                del st.session_state["chat_history"]
            st.rerun()
            
    st.header(":speech_balloon: Chat with your PDFs files", anchor="chat", divider="red")
    if "vectorstore" in st.session_state:
        st.success(":white_check_mark: The PDF file data has been loaded successfully. You are talking with: " + st.session_state["files_names"][:-2] + ".")
    else:
        st.error(":warning: The PDF file data has not been loaded yet.")
            
    if "vectorstore" in st.session_state:
        if "chat_history" not in st.session_state:
            st.session_state["chat_history"] = []
            welcome_message = "Hello there! I'm **Doc**, your friendly AI assistant here to help you chat with your PDF documents. Whether you need to find specific information, summarize content, or simply explore your document in a new way, I'm here to make it easy and fun! :rocket:"
            st.session_state["chat_history"].extend(
                [
                    AIMessage(content=welcome_message),
                ]
            )
            # st.write(ai_template.replace("{{MSG}}", "\n\n" + welcome_message), unsafe_allow_html=True)
        
        if user_message := st.chat_input(placeholder="What do you want to know about your documents?"):
            st.session_state["chat_history"].extend(
                [
                    HumanMessage(content=user_message),
                ]
            )
            # st.write(human_template.replace("{{MSG}}", "\n\n" + user_message), unsafe_allow_html=True)
            
            llm_response = ""
            for chunk in conversation_chain(user_message = user_message, vectorstore = st.session_state['vectorstore'],  chat_history = st.session_state["chat_history"]):
                llm_response += chunk

            st.session_state["chat_history"].extend(
                [
                    AIMessage(content=llm_response),
                ]
            )
            # st.write(ai_template.replace("{{MSG}}", "\n\n" + message.content), unsafe_allow_html=True)
        
        for message in st.session_state["chat_history"]:
            if isinstance(message, HumanMessage):
                st.write(human_template.replace("{{MSG}}", "\n\n" + message.content), unsafe_allow_html=True)
            elif isinstance(message, AIMessage):
                st.write(ai_template.replace("{{MSG}}", "\n\n" + message.content), unsafe_allow_html=True)
    else:
        pre_welcome_message = "Hello there! I'm **Doc**, your friendly AI assistant here to help you chat with your PDF documents. Whether you need to find specific information, summarize content, or simply explore your document in a new way, I'm here to make it easy and fun! :rocket:\n\nJust upload your PDF, and let’s get started! :page_with_curl:"
        st.write(ai_template.replace("{{MSG}}", "\n\n" + pre_welcome_message), unsafe_allow_html=True)

## EXECUÇÃO DO SCRIPT             
if __name__ == "__main__":
    generate_page()