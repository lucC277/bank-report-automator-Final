# exporter.py - Módulo para exportação de dados

import pandas as pd
import logging
from config import FINAL_REPORT_FILE, EXPENSE_CATEGORIES, ALERT_THRESHOLD
from datetime import datetime

# Configuração do logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataExporter:
    def __init__(self):
        self.final_report_file = FINAL_REPORT_FILE
        self.expense_categories = EXPENSE_CATEGORIES
        self.alert_threshold = ALERT_THRESHOLD

    def export_to_excel(self, processed_df, summary, filename=None):
        """
        Exporta os dados processados para um arquivo Excel

        Args:
            processed_df (pd.DataFrame): DataFrame com dados processados
            summary (dict): Dicionário com estatísticas de resumo
            filename (str): Nome do arquivo de saída (opcional)
        """
        if filename is None:
            filename = self.final_report_file

        try:
            with pd.ExcelWriter(filename, engine='openpyxl') as writer:
                # Aba com dados processados
                processed_df.to_excel(writer, sheet_name='Dados_Processados', index=False)

                # Aba com resumo
                if summary:
                    summary_df = pd.DataFrame(list(summary.items()), columns=['Métrica', 'Valor'])
                    summary_df.to_excel(writer, sheet_name='Resumo', index=False)

                # Aba com informações adicionais
                info_data = {
                    'Data_Geração': [datetime.now().strftime('%Y-%m-%d %H:%M:%S')],
                    'Total_Registros': [len(processed_df) if not processed_df.empty else 0],
                    'Arquivo_Origem': [filename]
                }
                info_df = pd.DataFrame(info_data)
                info_df.to_excel(writer, sheet_name='Informações', index=False)

            logger.info(f"Relatório exportado com sucesso para {filename}")

        except Exception as e:
            logger.error(f"Erro ao exportar relatório: {e}")

    def export_transactions_only(self, df, filename=None):
        """
        Exporta apenas as transações para Excel

        Args:
            df (pd.DataFrame): DataFrame a ser exportado
            filename (str): Nome do arquivo (opcional)
        """
        if filename is None:
            filename = self.final_report_file

        try:
            df.to_excel(filename, index=False, engine='openpyxl')
            logger.info(f"Transações exportadas para {filename}")
        except Exception as e:
            logger.error(f"Erro ao exportar transações: {e}")

    def create_formatted_report(self, processed_df, summary, filename=None):
        """
        Cria um relatório formatado com múltiplas abas e formatação

        Args:
            processed_df (pd.DataFrame): DataFrame processado
            summary (dict): Dicionário de resumo
            filename (str): Nome do arquivo (opcional)
        """
        if filename is None:
            filename = self.final_report_file

        try:
            with pd.ExcelWriter(filename, engine='openpyxl') as writer:
                # Aba principal com dados
                processed_df.to_excel(writer, sheet_name='Relatório_Principal', index=False)

                # Aba de resumo estatístico
                if summary:
                    summary_items = []
                    for key, value in summary.items():
                        if isinstance(value, dict):
                            # Para dicionários aninhados (como despesas por categoria)
                            for sub_key, sub_value in value.items():
                                summary_items.append([f"{key}_{sub_key}", sub_value])
                        else:
                            summary_items.append([key, value])

                    summary_df = pd.DataFrame(summary_items, columns=['Métrica', 'Valor'])
                    summary_df.to_excel(writer, sheet_name='Resumo_Estatístico', index=False)

                # Aba de categorias de despesa
                if summary and 'expenses_by_category' in summary:
                    categories_data = []
                    for category in self.expense_categories:
                        amount = summary['expenses_by_category'].get(category, 0)
                        categories_data.append([category, amount])

                    categories_df = pd.DataFrame(categories_data, columns=['Categoria', 'Valor Total (BRL)'])
                    categories_df.to_excel(writer, sheet_name='Despesas_por_Categoria', index=False)

                # Aba de alertas
                if summary and 'alert_transactions' in summary and summary['alert_transactions']:
                    alerts_df = pd.DataFrame(summary['alert_transactions'])
                    alerts_df.to_excel(writer, sheet_name='Alertas', index=False)

                # Aba de metadados
                metadata = {
                    'Título': ['Relatório de Transações Bancárias'],
                    'Data de Geração': [datetime.now().strftime('%d/%m/%Y %H:%M:%S')],
                    'Total de Registros': [len(processed_df)],
                    'Moeda Base': [summary.get('moeda_alvo', 'N/A') if summary else 'N/A'],
                    'Valor Total': [summary.get('total_valor', 0) if summary else 0],
                    'Threshold de Alerta': [f'R$ {self.alert_threshold}'],
                    'Total de Alertas': [summary.get('alerts', 0) if summary else 0]
                }
                metadata_df = pd.DataFrame(metadata)
                metadata_df.to_excel(writer, sheet_name='Metadados', index=False)

            logger.info(f"Relatório formatado criado em {filename}")

        except Exception as e:
            logger.error(f"Erro ao criar relatório formatado: {e}")

if __name__ == "__main__":
    # Exemplo de uso
    exporter = DataExporter()

    # Cria um DataFrame de exemplo
    sample_data = {
        'Data': ['2023-01-01', '2023-01-02', '2023-01-03'],
        'Descrição': ['Transação 1', 'Transação 2', 'Transação 3'],
        'Valor': [100.0, 200.0, 150.0],
        'Moeda': ['USD', 'EUR', 'USD'],
        'Valor_Convertido': [500.0, 1100.0, 750.0],
        'Moeda_Alvo': ['BRL', 'BRL', 'BRL']
    }
    sample_df = pd.DataFrame(sample_data)

    sample_summary = {
        'total_valor': 2350.0,
        'media_valor': 783.33,
        'num_transacoes': 3,
        'moeda_alvo': 'BRL'
    }

    exporter.create_formatted_report(sample_df, sample_summary)

# Função para uso direto (conforme esperado pelo main.py)
def export_report(summary, rates):
    """
    Função que exporta o relatório final

    Args:
        summary (dict): Resumo das transações
        rates (dict): Cotações das moedas
    """
    # Import necessário
    from .processor import DataProcessor

    # Carrega os dados processados
    processor = DataProcessor()
    processed_data, _ = processor.process_all()

    if processed_data.empty:
        # Cria dados de exemplo se não houver dados processados
        processed_data = pd.DataFrame({
            'Data': ['2024-01-01'],
            'Descrição': ['Exemplo'],
            'Valor': [100.0],
            'Moeda': ['USD'],
            'Valor_Convertido': [520.0],
            'Moeda_Alvo': ['BRL'],
            'Tipo': ['Exemplo']
        })

    # Adiciona informações de cotações ao resumo
    enhanced_summary = summary.copy()
    enhanced_summary.update({
        'cotacao_usd': rates.get('USD', 5.20),
        'cotacao_eur': rates.get('EUR', 6.10),
    })

    exporter = DataExporter()
    exporter.create_formatted_report(processed_data, enhanced_summary)