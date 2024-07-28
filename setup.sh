#!/bin/bash

# Saída imediata em caso de erro
set -e

# Instalar pip e venv, caso ainda não estejam instalados
echo "Atualizando lista de pacotes e instalando python3-pip e python3-venv..."
sudo apt-get update && sudo apt-get install -y python3-pip python3-venv

# Criar um ambiente virtual
echo "Criando o ambiente virtual..."
python3 -m venv venv

# Ativar o ambiente virtual
echo "Ativando o ambiente virtual..."
source venv/bin/activate

# Instalar as dependências
echo "Instalando as dependências..."
pip install -r requirements.txt

# Executar o Streamlit
echo "Executando o Streamlit..."
python3 -m streamlit run src/app.py
