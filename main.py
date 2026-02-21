import pandas as pd
from pathlib import Path

arquivo = Path("data/alunos.xlsx")

if not arquivo.exists():
    raise FileNotFoundError(f"Arquivo não encontrado: {arquivo}")

abas = pd.read_excel(arquivo, sheet_name=None)

print(f"total de abas encontradas: {len(abas)}")
print(f"nome das abas: {list(abas.keys())}")
print()

for nome_aba, df in abas.items():
    print('=' * 50)
    print(f"Aba: {nome_aba}")
    print("\nPrévia")
    print(df.head())

    print("\nColunas:", df.columns.tolist())
    print("\nTipos:")
    print(df.dtypes())
    
    print("\nValores faltantes:")
    print(df.isna().sum())