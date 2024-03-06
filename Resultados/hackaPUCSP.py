
import pandas as pd
import os
import shutil
import re
# Caminho da pasta original
pasta_origem = '/content/drive/MyDrive/strings-de-busca-ods.zip (Unzipped Files)'

# Criar uma nova pasta no Google Drive
nova_pasta = 'Nova_Pasta_Ods'
os.makedirs(nova_pasta, exist_ok=True)

# Lista de arquivos na pasta original
arquivos_na_pasta_origem = os.listdir(pasta_origem)

# Criar um dicionário de caminhos para os arquivos na nova pasta
caminhos = {}
for i, arquivo in enumerate(arquivos_na_pasta_origem, start=1):
    if arquivo.lower().endswith('.txt'):  # Verificar se o arquivo é do tipo txt
        nome_arquivo = f'ods{i:02d}.txt'  # Formatação para garantir dois dígitos (ex: 'ods01.txt')
        caminho_origem = os.path.join(pasta_origem, arquivo)
        caminho_destino = os.path.join(nova_pasta, nome_arquivo)

        # Copiar arquivo original para a nova pasta
        shutil.copy2(caminho_origem, caminho_destino)  # Usar shutil.copy2 para preservar metadados

        caminhos[f'ods{i:02d}'] = caminho_destino

# Iterar sobre o dicionário para carregar e processar os arquivos
for nome, caminho in caminhos.items():
    df = pd.read_csv(caminho, delimiter='\t')
    df = df.apply(lambda x: x.str.strip() if x.dtype == 'object' else x)

    # Substituir palavras no DataFrame usando o dicionário alteracao
    alteracao = {
    "OU": "or",
    "E": "and",
    "NÃO": "not"
}
    # Fazer alterações no arquivo, como traduzir para o inglês as condições e tirar as barras e as chaves
    nome_coluna = df.columns[0] if len(df.columns) > 0 else None

    if nome_coluna is not None:
        df[nome_coluna] = df[nome_coluna].str.replace('|'.join(alteracao.keys()), lambda x: alteracao[x.group()], regex=True)
        df[nome_coluna] = df[nome_coluna].replace(r'[{}]', '', regex=True)
        df[nome_coluna] = df[nome_coluna].replace(r'/', ' ', regex=True)

        # Substituir o nome da coluna com base no nome do arquivo
        novo_nome_coluna = f'{nome}'  # Adapte conforme necessário
        df.rename(columns={nome_coluna: novo_nome_coluna}, inplace=True)

        # Copiar o DataFrame modificado para um novo arquivo na pasta de destino
        novo_caminho_destino = os.path.join(nova_pasta, f'{nome}_modificado.txt')
        df.to_csv(novo_caminho_destino, sep='\t', index=False)

    print(f"Dataframe para {nome} após substituição:")
    print(df)

    # Se necessário, realizar o processamento adicional aqui (por exemplo, remover valores vazios)
    df_sem_vazios = df.dropna(axis=1, how='all')

treino = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/train_df.tsv', sep='\t')
teste = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/test_df1.tsv', sep='\t')

# Caminho da pasta com os arquivos das ODS modificadas
pasta_ods_modificadas = 'Nova_Pasta_Ods'

# Criar um dicionário para armazenar os DataFrames das ODS modificadas
ods = {}

# Iterar sobre os arquivos na pasta de ODS modificadas
for arquivo_ods in os.listdir(pasta_ods_modificadas):
    if arquivo_ods.lower().endswith('_modificado.txt'):
        # Extrair o nome da ODS do nome do arquivo
        ods_nome = re.match(r'ods(\d+)_modificado\.txt', arquivo_ods.lower())
        if ods_nome:
            ods_nome = f'ods{ods_nome.group(1)}'
            caminho_arquivo_ods = os.path.join(pasta_ods_modificadas, arquivo_ods)
            # Ler o arquivo como DataFrame e armazenar no dicionário
            ods[ods_nome] = pd.read_csv(caminho_arquivo_ods, delimiter='\t')

# Supondo que você tenha um DataFrame chamado "teses" com as teses a serem classificadas
# Exemplo:
teses = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/train_df.tsv', delimiter='\t')
teses['ODS'] = ''  # Adiciona uma coluna 'ODS' vazia para armazenar os resultados
colunas = teses.columns

# Dicionário para armazenar as teses classificadas para cada ODS
teses_classificadas = {key: [] for key in ods.keys()}

# Percorre cada tese e classifica de acordo com as chaves de busca de cada ODS
for ods_nome, ods_df in ods.items():
    # Obter colunas específicas associadas à ODS (pode haver mais de uma coluna)
    colunas_chaves = [ods_nome]  # Adicione mais colunas se necessário

    # Lista de listas de palavras-chave para a ODS (uma lista para cada coluna)
    palavras_chave_listas = [ods_df[col].dropna().tolist() for col in colunas_chaves]
    for index, tese_row in teses.iterrows():
        texto_tese = str(tese_row['palavras_chave'])  # Supondo que o texto da tese está na coluna 'Texto'

        # Verifica se o texto da tese contém pelo menos uma palavra-chave de cada coluna da ODS
        if all(
            any(re.search(fr'\b{re.escape(palavra)}\b', texto_tese, flags=re.IGNORECASE) for palavra in palavras_chave)
            for palavras_chave in palavras_chave_listas
        ):
            teses_classificadas[ods_nome].append(index)
            teses.at[index, 'ODS'] = ods_nome  # Adiciona a ODS correspondente à coluna 'ODS'

# Criar um objeto ExcelWriter para salvar as teses classificadas
excel_writer = pd.ExcelWriter('teses_classificadas.xlsx', engine='xlsxwriter')

# Iterar sobre as ODS e salvar as teses classificadas em abas separadas
for ods_nome, indices_teses in teses_classificadas.items():
    print(f'Teses classificadas para {ods_nome}:')
    # Selecionar as teses classificadas para a ODS atual
    teses_ods = teses.iloc[indices_teses]
    # Salvar no ExcelWriter
    teses_ods.to_excel(excel_writer, sheet_name=ods_nome, index=False)
    print('\n')

# Fechar o ExcelWriter para salvar o arquivo
excel_writer.save()
# ... (código anterior)

# Percorre cada tese e classifica de acordo com as chaves de busca de cada ODS
for ods_nome, ods_df in ods.items():
    # Obter colunas específicas associadas à ODS (pode haver mais de uma coluna)
    colunas_chaves = [ods_nome]  # Adicione mais colunas se necessário

    # Lista de listas de palavras-chave para a ODS (uma lista para cada coluna)
    palavras_chave_listas = [ods_df[col].dropna().tolist() for col in colunas_chaves]
    print(palavras_chave_listas)

    for index, tese_row in teses.iterrows():
        texto_tese = str(tese_row['palavras_chave'])  # Supondo que o texto da tese está na coluna 'Texto'

        # Verifica se o texto da tese contém pelo menos uma palavra-chave de cada coluna da ODS
        if all(
            any(re.search(fr'\b{re.escape(palavra)}\b', texto_tese, flags=re.IGNORECASE) for palavra in palavras_chaves)
            for palavras_chaves in palavras_chave_listas
        ):
            teses_classificadas[ods_nome].append(index)
            teses.at[index, 'ODS'] = ods_nome  # Adiciona a ODS correspondente à coluna 'ODS'

# Percorre cada tese e classifica de acordo com as chaves de busca de cada ODS
for ods_nome, ods_df in ods.items():
    # Obter colunas específicas associadas à ODS (pode haver mais de uma coluna)
    colunas_chaves = [ods_nome]  # Adicione mais colunas se necessário

    # Lista de listas de palavras-chave para a ODS (uma lista para cada coluna)
    palavras_chave_listas = [ods_df[col].dropna().tolist() for col in colunas_chaves]

    for index, tese_row in teses.iterrows():
        texto_tese = str(tese_row['palavras_chave'])  # Supondo que o texto da tese está na coluna 'palavras_chave'

        print(f'Tese #{index + 1} - ODS: {ods_nome}')
        print(f'Texto da Tese: {texto_tese}')

        # Verifica se o texto da tese contém pelo menos uma palavra-chave de cada coluna da ODS
        if all(
            any(re.search(fr'\b{re.escape(palavra)}\b', texto_tese, flags=re.IGNORECASE) for palavra in palavras_chaves)
            for palavras_chaves in palavras_chave_listas
        ):
            teses_classificadas[ods_nome].append(index)
            teses.at[index, 'ODS'] = ods_nome  # Adiciona a ODS correspondente à coluna 'ODS'
            print('Classificada!\n')
        else:
            print('Não classificada.\n')

# Criar um objeto ExcelWriter para salvar as teses classificadas
excel_writer = pd.ExcelWriter('teses_classificadas.xlsx', engine='xlsxwriter')

# Dicionário para armazenar o número de teses classificadas para cada ODS
num_teses_classificadas = {}

# Iterar sobre as ODS e salvar as teses classificadas em abas separadas
for ods_nome, indices_teses in teses_classificadas.items():
    print(f'Teses classificadas para {ods_nome}:')
    # Selecionar as teses classificadas para a ODS atual
    teses_ods = teses.iloc[indices_teses]
    # Salvar no ExcelWriter
    teses_ods.to_excel(excel_writer, sheet_name=ods_nome, index=False)
    num_teses_classificadas[ods_nome] = len(indices_teses)  # Armazenar o número de teses classificadas
    print(f'Número de teses classificadas para {ods_nome}: {len(indices_teses)}\n')

# Imprimir a contagem total de teses classificadas para cada ODS ao final do processo
print('\nResumo:')
for ods_nome, num_teses in num_teses_classificadas.items():
    print(f'{ods_nome}: {num_teses} teses classificadas')

# Fechar o ExcelWriter para salvar o arquivo
excel_writer.save()
