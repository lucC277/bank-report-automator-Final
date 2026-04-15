# config.py - Configurações do projeto Bank Report Automator

import os

# Caminhos dos arquivos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
REPORTS_DIR = os.path.join(BASE_DIR, 'reports')

# Arquivos de dados
TRANSACTIONS_FILE = os.path.join(DATA_DIR, 'transacoes.csv')
EXCHANGE_RATES_FILE = os.path.join(DATA_DIR, 'cotacoes.xlsx')
FINAL_REPORT_FILE = os.path.join(REPORTS_DIR, 'relatorio_final.xlsx')

# APIs do Banco Central do Brasil
USD_API_URL = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.10813/dados?formato=json"
EUR_API_URL = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.21619/dados?formato=json"

# Configurações de processamento
DEFAULT_CURRENCY = "USD"
TARGET_CURRENCY = "BRL"
REPORT_MONTH = "2026-03"  # Mês do relatório

# Parâmetros
ALERT_THRESHOLD = 300.00  # Valor para alertas

# Categorias de despesa
EXPENSE_CATEGORIES = [
    "Alimentação",
    "Transporte",
    "Lazer",
    "Saúde",
    "Educação"
]

# Configurações de logging
LOG_LEVEL = "INFO"
LOG_FILE = os.path.join(BASE_DIR, 'bank_report.log')