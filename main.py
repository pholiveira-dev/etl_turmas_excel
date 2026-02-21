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

# Total de alunos:
print(f"Total de alunos: {len(df)}")

# Media geral
media_geral = df['Nota'].mean()
print(f"Média geral: {media_geral}")

# Media por curso:
media_curso = df.groupby("Curso")["Nota"].mean()
print(media_curso)

# Taxa aprovação:
taxa_aprovacao = df['Situacao'].value_counts(normalize=True) * 100
print(taxa_aprovacao)

top_5 = df.sort_values("Nota", ascending=False).head(5)
print(top_5)