import pandas as pd
from pathlib import Path


def carregar_dados(caminho):
    if not caminho.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")

    abas = pd.read_excel(caminho, sheet_name=None)

    lista_dfs = []

    for nome_aba, df in abas.items():
        df = df.copy()
        df["Grupo"] = nome_aba
        df["Nome"] = df["Nome"].str.upper()
        df["Nota"] = pd.to_numeric(df["Nota"], errors="coerce")
        df["Situacao"] = df["Nota"].apply(
            lambda x: "Aprovado" if x >= 7 else "Reprovado"
        )
        lista_dfs.append(df)

    return pd.concat(lista_dfs, ignore_index=True)


def analisar(df):
    total_alunos = len(df)
    media_geral = df["Nota"].mean()
    media_curso = df.groupby("Curso")["Nota"].mean()
    taxa_aprovacao = df["Situacao"].value_counts(normalize=True) * 100
    top_5 = df.sort_values("Nota", ascending=False).head(5)

    print(f"\nTotal alunos: {total_alunos}")
    print(f"Média geral: {media_geral:.2f}")
    print("\nMédia por curso:")
    print(media_curso)
    print("\nTaxa aprovação:")
    print(taxa_aprovacao)
    print("\nTop 5:")
    print(top_5)

    return total_alunos, media_geral, media_curso, taxa_aprovacao, top_5


def exportar(df, total, media, media_curso, taxa, top5):
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    df.to_csv(output_dir / "dataset_final.csv", index=False)
    df.to_excel(output_dir / "dataset_final.xlsx", index=False)

    resumo_df = pd.DataFrame({
        "metrica": ["total_alunos", "media_geral"],
        "valor": [total, media]
    })

    media_df = media_curso.reset_index(name="media_nota")

    taxa_df = taxa.reset_index()
    taxa_df.columns = ["Situacao", "Percentual"]

    top5_df = top5[["Nome", "Curso", "Nota"]]

    with pd.ExcelWriter(output_dir / "relatorio_resumo.xlsx", engine="openpyxl") as writer:
        resumo_df.to_excel(writer, sheet_name="Resumo Geral", index=False)
        media_df.to_excel(writer, sheet_name="Media por Curso", index=False)
        taxa_df.to_excel(writer, sheet_name="Taxa Aprovacao", index=False)
        top5_df.to_excel(writer, sheet_name="Top 5", index=False)


def main():
    arquivo = Path("data/alunos.xlsx")

    df = carregar_dados(arquivo)

    total, media, media_curso, taxa, top5 = analisar(df)

    exportar(df, total, media, media_curso, taxa, top5)

    print("\nPipeline executado com sucesso 🚀")


if __name__ == "__main__":
    main()