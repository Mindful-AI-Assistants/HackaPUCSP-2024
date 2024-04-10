# Define a imagem base
FROM ghcr.io/containerbase/devcontainer:10.1.4

# Atualiza a lista de pacotes
RUN apt-get update

# Instala as dependências necessárias (substitua 'my-package' pelas suas dependências)
RUN apt-get install -y my-package

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto para o contêiner
COPY . .

# Comando para iniciar o aplicativo (substitua 'my-command' pelo seu comando)
CMD ["my-command"]






