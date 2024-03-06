import os
import re
from typing import Dict
import pandas as pd

def classify_theses(ods: Dict[str, pd.DataFrame], teses: pd.DataFrame) -> Dict[str, list]:

    """
    Classify theses based on ODS keywords.
    """

    teses_classificadas = {key: [] for key in ods.keys()}

    for ods_nome, ods_df in ods.items():
        colunas_chaves = [ods_nome]
        palavras_chave_listas = [
            ods_df[col].dropna().tolist() for col in colunas_chaves
        ]

        for index, tese_row in teses.iterrows():
            texto_tese = str(tese_row['palavras_chave'])

            if all(
                any(
                    re.search(
                        fr'\b{re.escape(palavra)}\b',
                        texto_tese,
                        flags=re.IGNORECASE
                    )
                    for palavra in palavras_chaves
                )
                for palavras_chaves in palavras_chave_listas
            ):
                teses_classificadas[ods_nome].append(index)
                teses.at[index, 'ODS'] = ods_nome

    return teses_classificadas


def process_file(name: str, path: str, new_folder: str) -> pd.DataFrame:

    """
    Process a file and return a DataFrame.
    """

    df = pd.read_csv(path, delimiter='\t')
    df = df.apply(lambda x: x.str.strip() if x.dtype == 'object' else x)

    replacements = {
        "OU": "or",
        "E": "and",
        "NÃO": "not"
    }

    column_name = df.columns[0] if len(df.columns) > 0 else None

    if column_name is not None:
        df[column_name] = df[column_name].str.replace(
            '|'.join(replacements.keys()),
            lambda x: replacements[x.group()],
            regex=True
        )
        df[column_name] = df[column_name].replace(r'[{}]', '', regex=True)
        df[column_name] = df[column_name].replace(r'/', ' ', regex=True)

        new_column_name = f'{name}'
        df.rename(columns={column_name: new_column_name}, inplace=True)

        new_destination_path = os.path.join(new_folder, f'{name}_modified.txt')
        df.to_csv(new_destination_path, sep='\t', index=False)

    print(f"Dataframe for {name} after replacement:")
    print(df)

    df_no_empty = df.dropna(axis=1, how='all')
    return df_no_empty


def process_files(file_paths: Dict[str, str], new_folder: str) -> Dict[str, pd.DataFrame]:

    """
    Process multiple files and return a dictionary of DataFrames.
    """

    processed_files = {}
    for name, path in file_paths.items():
        processed_files[name] = process_file(name, path, new_folder)
    return processed_files


def save_classified_theses_to_excel(teses_classificadas: Dict[str, list], file_name: str, teses: pd.DataFrame) -> None:

    """
    Save classified theses to an Excel file.
    """

    excel_writer = pd.ExcelWriter(file_name, engine='xlsxwriter')

    num_teses_classificadas = {}

    for ods_nome, indices_teses in teses_classificadas.items():
        teses_ods = teses.iloc[indices_teses]
        teses_ods.to_excel(excel_writer, sheet_name=ods_nome, index=False)
        num_teses_classificadas[ods_nome] = len(indices_teses)

    excel_writer.save()

    print('\nSummary:')
    for ods_nome, num_teses in num_teses_classificadas.items():
        print(f'{ods_nome}: {num_teses} theses classified')


# Use the functions
file_paths = {
    # Add your file paths here
    # 'file_name': 'file_path'
}

NEW_FOLDER = '/path/to/new/folder'

processed_files = process_files(file_paths, NEW_FOLDER)

train = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/train_df.tsv', sep='\t')
test = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/test_df1.tsv', sep='\t')

classified_theses = classify_theses(processed_files, train)

save_classified_theses_to_excel(classified_theses, 'classified_theses.xlsx', train)
