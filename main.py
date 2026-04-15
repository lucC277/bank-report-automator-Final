#!/usr/bin/env python3
"""Bank Report Automator — RPA para relatórios financeiros
Coleta dados, processa transações e gera relatórios Excel automaticamente.
"""

import sys
import os
from src.collector import collect_exchange_rates
from src.processor import process_transactions
from src.exporter import export_report
from config import REPORT_MONTH

def main():
    print("🏦 Bank Report Automator")
    print("========================")

    try:
        # 1. Coletar cotações
        print("📡 Coletando cotações...")
        rates = collect_exchange_rates()
        print(f"✅ USD: R$ {rates.get('USD', 'N/A')} | EUR: R$ {rates.get('EUR', 'N/A')}")

        # 2. Processar transações
        print(f"\n📊 Processando transações de {REPORT_MONTH}...")
        summary = process_transactions()
        print(f"✅ {summary['total_transactions']} transações processadas")
        print(f"   Entradas: R$ {summary['total_income']:.2f}")
        print(f"   Saídas:   R$ {summary['total_expenses']:.2f}")
        print(f"   Saldo:    R$ {summary['balance']:.2f}")

        # 3. Gerar relatório
        print(f"\n📋 Gerando relatório Excel...")
        export_report(summary, rates)
        print("✅ Relatório gerado com sucesso!")

        print(f"\n🎉 RPA concluído! Arquivo: reports/relatorio_final.xlsx")

    except Exception as e:
        print(f"❌ Erro: {e}")
        return 1

    return 0

if __name__ == "__main__":
    sys.exit(main())