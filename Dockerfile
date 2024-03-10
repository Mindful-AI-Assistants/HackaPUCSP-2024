

# Use a imagem oficial do Python a partir do Docker Hub
FROM python:3.11-slim-buster

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia os arquivos do diretório atual para o contêiner
COPY . .

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt


