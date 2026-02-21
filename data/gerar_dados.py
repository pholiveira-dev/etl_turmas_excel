import pandas as pd
from pathlib import Path

Path('data').mkdir(exist_ok=True)

grupo1 = pd.DataFrame({
    "Nome": ['João', 'Ana', 'Carlos'],
    "Idade": [21, 20, 22],
    "Curso": ['Enfermagem', 'Nutrição', 'Fisioterapia'],
    "Nota": [8.5, 9.0, 7.8]
})

grupo2 = pd.DataFrame({
    "Nome": ['Mariana', 'Lucas', 'Fernanda'],
    "Idade": [23, 19, 21],
    "Curso": ['Enfermagem', 'Nutrição', 'Fisioterapia'],
    "Nota": [8.8, 7.5, 9.3]
})

grupo3 = pd.DataFrame({
    "Nome": ['Rafael', 'Juliana', 'Bruno'],
    "Idade": [22, 24, 20],
    "Curso": ['Enfermagem', 'Nutrição', 'Fisioterapia'],
    "Nota": [6.9, 8.1, 7.4]
})

grupo4 = pd.DataFrame({
    "Nome": ['Patricia', 'Diego', 'Sofia'],
    "Idade": [21, 23, 19],
    "Curso": ['Enfermagem', 'Nutrição', 'Fisioterapia'],
    "Nota": [9.1, 6.8, 8.7]   
})

arquivo = 'data/alunos.xlsx'

# salvar as múltiplas abas

with pd.ExcelWriter(arquivo, engine='openpyxl') as writer:
    grupo1.to_excel(writer, sheet_name="Grupo1", index=False)
    grupo2.to_excel(writer, sheet_name="Grupo2", index=False)
    grupo3.to_excel(writer, sheet_name="Grupo3", index=False)
    grupo4.to_excel(writer, sheet_name="Grupo4", index=False)

print("Excel criado com sucesso em:", arquivo)