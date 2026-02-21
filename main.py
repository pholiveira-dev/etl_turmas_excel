import pandas as pd
from pathlib import Path

arquivo = Path("data/alunos.xlsx")

if not arquivo.exists():
    raise FileNotFoundError(f"Arquivo não encontrado: {arquivo}")

abas = pd.read_excel(arquivo, sheet_name=None)

lista_dfs = []

for nome_aba, df in abas.items():

    df = df.copy()

    df["Grupo"] = nome_aba

    df["Nome"] = df["Nome"].str.upper()

    df["Nota"] = pd.to_numeric(df["Nota"], errors="coerce")

    df["Situacao"] = df["Nota"].apply(lambda x: "Aprovado" if x >= 7 else "Reprovado")

    lista_dfs.append(df)

df_final = pd.concat(lista_dfs, ignore_index=True)

print(df_final)