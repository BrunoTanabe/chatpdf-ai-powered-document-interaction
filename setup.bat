@echo off

echo Instalando o pip e o venv...
python -m ensurepip --upgrade

echo Criando um ambiente virtual...
python -m venv venv

echo Ativando o ambiente virtual...
call venv\Scripts\activate

echo Instalando as dependências...
pip install -r requirements.txt

echo Executando o Streamlit...
python -m streamlit run src/app.py

pause
