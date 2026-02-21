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

# =============================
# ANALISES
# =============================

total_alunos = len(df_final)
print(f"Total de alunos: {total_alunos}")

media_geral = df_final['Nota'].mean()
print(f"Média geral: {media_geral}")

media_curso = df_final.groupby("Curso")["Nota"].mean()
print(media_curso)

taxa_aprovacao = df_final['Situacao'].value_counts(normalize=True) * 100
print(taxa_aprovacao)

top_5 = df_final.sort_values("Nota", ascending=False).head(5)
print(top_5)


# =============================
# EXPORT
# =============================

output_dir = Path("output")
output_dir.mkdir(exist_ok=True)

df_final.to_csv(output_dir / "dataset_final.csv", index=False)
df_final.to_excel(output_dir / "dataset_final.xlsx", index=False)

media_por_curso_df = media_curso.reset_index(name="media_nota")

taxa_aprovacao_df = taxa_aprovacao.reset_index()
taxa_aprovacao_df.columns = ['Situacao', 'Percentual']

top_5_df = top_5[["Nome", "Curso", "Nota"]]

resumo_df = pd.DataFrame({
    "metrica": ["total_alunos", "media_geral"],
    "valor": [total_alunos, media_geral]
})

with pd.ExcelWriter(output_dir / "relatorio_resumo.xlsx", engine="openpyxl") as writer:
    resumo_df.to_excel(writer, sheet_name="Resumo Geral", index=False)
    media_por_curso_df.to_excel(writer, sheet_name="Média por Curso", index=False)
    taxa_aprovacao_df.to_excel(writer, sheet_name="Taxa Aprovação", index=False)
    top_5_df.to_excel(writer, sheet_name="Top 5", index=False)

print("\nArquivos exportados com sucesso em /output")