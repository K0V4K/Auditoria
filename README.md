<div align="center">
  <h1>📄 Processador e Análise de Invoices (PDF)</h1>
  <p><strong>Desafio Técnico: Extração, Validação e Análise de Dados com Python</strong></p>
  
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Pandas-1.5+-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/Pydantic-Data--Validation-red?style=for-the-badge&logo=pydantic&logoColor=white" alt="Pydantic">
</div>

<hr>

## 🎯 Objetivos do Projeto
Este projeto foi desenvolvido para demonstrar competências em **Engenharia de Dados** e automação. O sistema realiza o fluxo completo de um pipeline de dados (ETL):
* **Extração:** Captura de dados estruturados de arquivos PDF.
* **Validação:** Garantia da integridade dos dados capturados.
* **Persistência:** Armazenamento em JSON para consumo posterior.
* **Análise:** Geração de insights estratégicos com métricas de vendas.

## 🛠️ Tecnologias Utilizadas
<ul>
  <li><strong>Python 3.10+</strong>: Linguagem base.</li>
  <li><strong>Pydantic</strong>: Validação de dados e modelos.</li>
  <li><strong>Pandas</strong>: Análise e processamento de dados.</li>
  <li><strong>pdfplumber</strong>: Extração precisa de texto em PDFs.</li>
  <li><strong>JSON</strong>: Banco de dados local.</li>
</ul>

## 🏗️ Arquitetura do Sistema
O projeto segue uma estrutura modular para facilitar a manutenção:

```text
Teste Técnico-QCA/
├── invoices/              # PDFs de entrada
├── ingest/                # Módulo de Processamento
│   ├── models.py          # Modelos Pydantic
│   ├── pdf_reader.py      # Lógica de leitura
│   └── repository.py      # Gestão do JSON
├── analytics/             # Módulo de Inteligência
│   └── analytics.py       # Análises com Pandas
├── database.json          # Base de dados gerada
├── main.py                # Ponto de entrada
└── requirements.txt       # Dependências
