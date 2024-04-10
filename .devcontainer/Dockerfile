# Define a imagem base
FROM ghcr.io/containerbase/devcontainer:10.1.4

# Atualiza a lista de pacotes
RUN apt-get update

# Instala o Python e o pip
RUN apt-get install -y python3 python3-pip

# Copia o arquivo de requisitos para o contêiner
COPY requirements.txt .

# Instala as bibliotecas Python listadas no arquivo de requisitos
RUN pip3 install -r requirements.txt

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto para o contêiner
COPY . .

# Comando para iniciar o aplicativo (substitua 'my_script.py' pelo seu script Python)
CMD ["python3", "my_script.py"]
