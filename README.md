# 📊 Pipeline de Dados com Python e Pandas

Projeto de **pipeline ETL simples** desenvolvido em Python para leitura de planilhas Excel com múltiplas abas, consolidação de dados, geração de métricas analíticas e exportação de relatórios finais.

O objetivo do projeto é demonstrar habilidades iniciais em **Engenharia de Dados**, incluindo ingestão, transformação, análise e exportação de dados de forma reproduzível.

---

## 🚀 Funcionalidades

- ✔ Leitura automática de planilha Excel com múltiplas abas
- ✔ Consolidação dos dados em um único DataFrame
- ✔ Limpeza e padronização de colunas
- ✔ Conversão segura de tipos numéricos
- ✔ Criação de coluna derivada (_Situação do aluno_)
- ✔ Cálculo de métricas analíticas:
  - Total de registros
  - Média geral das notas
  - Média por curso
  - Taxa de aprovação
  - Ranking dos melhores alunos

- ✔ Exportação dos resultados em:
  - CSV final consolidado
  - Excel final consolidado
  - Excel de relatório com múltiplas abas

---

## 🗂 Estrutura do Projeto

```
projeto/
│
├── data/
│   └── alunos.xlsx              # Planilha de entrada
│
├── output/
│   ├── dataset_final.csv
│   ├── dataset_final.xlsx
│   └── relatorio_resumo.xlsx
│
├── main.py                      # Script principal do pipeline
└── README.md
```

---

## ⚙️ Tecnologias utilizadas

- Python 3
- Pandas
- Openpyxl
- Pathlib

---

## ▶️ Como executar o projeto

### 1️⃣ Clone o repositório

```
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_PROJETO>
```

### 2️⃣ Instale as dependências

```
pip install pandas openpyxl
```

### 3️⃣ Execute o pipeline

```
python main.py
```

---

## 📥 Entrada de dados

O pipeline espera um arquivo:

```
data/alunos.xlsx
```

Com:

- múltiplas abas
- mesmas colunas em cada aba:
  - Nome
  - Idade
  - Curso
  - Nota

Cada aba representa um **grupo diferente de alunos**.

---

## 📤 Saída gerada

Após execução, será criada automaticamente a pasta:

```
output/
```

Contendo:

### 📄 dataset_final.csv

Dados consolidados prontos para consumo por sistemas.

### 📊 dataset_final.xlsx

Versão Excel do dataset final.

### 📑 relatorio_resumo.xlsx

Relatório analítico com abas:

- Resumo Geral
- Média por Curso
- Taxa de Aprovação
- Top 5 alunos

---

## 🧠 Conceitos de Engenharia de Dados demonstrados

- Ingestão de dados estruturados
- Processamento multi-sheet Excel
- Data cleaning
- Feature engineering
- Agregações analíticas
- Exportação estruturada
- Pipeline reproduzível

---

## 🎯 Objetivo educacional

Este projeto foi desenvolvido como prática de:

- manipulação de dados com Pandas
- estruturação de pipelines simples
- preparação para vagas de **Engenharia de Dados Júnior / Estágio**

---

## 👨‍💻 Autor

Pedro Henrique

---

## 📌 Possíveis melhorias futuras

- leitura de dados via API pública
- armazenamento em banco SQL
- logs estruturados
- testes automatizados
- containerização com Docker
- orquestração com Airflow

---
