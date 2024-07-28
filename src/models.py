# models.py: Script para criar os modelos de chatbot do LangChain

## IMPORTAÇÃO DOS PACOTES NECESSÁRIOS
### Pacotes do Python
import os
from dotenv import load_dotenv
### Pacotes do LangChain
from langchain_groq import ChatGroq

## CARREGAMENTO DAS VARIÁVEIS DE AMBIENTE
### Ajuste do caminho para o arquivo .env e importação das variáveis de ambiente
dotenv_path = os.path.join(os.path.dirname(__file__), '..', 'config', '.env')
load_dotenv(dotenv_path)

## CONFIGURAÇÃO DOS MODELOS
### Configuração do llama3
llama3_model = ChatGroq(
    model=os.getenv("LLAMA3_MODEL"),
    api_key=os.getenv("LLAMA3_API_KEY"),
    temperature=os.getenv("LLAMA3_TEMPERATURE"),
)