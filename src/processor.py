# processor.py - Módulo para processamento de dados

import pandas as pd
import logging
from config import TRANSACTIONS_FILE, EXCHANGE_RATES_FILE, TARGET_CURRENCY, EXPENSE_CATEGORIES, ALERT_THRESHOLD
from datetime import datetime

# Configuração do logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataProcessor:
    def __init__(self):
        self.transactions_file = TRANSACTIONS_FILE
        self.exchange_rates_file = EXCHANGE_RATES_FILE
        self.target_currency = TARGET_CURRENCY
        self.expense_categories = EXPENSE_CATEGORIES
        self.alert_threshold = ALERT_THRESHOLD

    def load_transactions(self):
        """
        Carrega as transações do arquivo CSV

        Returns:
            pd.DataFrame: DataFrame com as transações
        """
        try:
            df = pd.read_csv(self.transactions_file)
            logger.info(f"Transações carregadas: {len(df)} registros")
            return df
        except Exception as e:
            logger.error(f"Erro ao carregar transações: {e}")
            return pd.DataFrame()

    def load_exchange_rates(self):
        """
        Carrega as cotações do arquivo Excel

        Returns:
            pd.DataFrame: DataFrame com as cotações
        """
        try:
            df = pd.read_excel(self.exchange_rates_file, sheet_name='Cotações')
            logger.info(f"Cotações carregadas: {len(df)} registros")
            return df
        except Exception as e:
            logger.error(f"Erro ao carregar cotações: {e}")
            return pd.DataFrame()

    def convert_currency(self, amount, from_currency, to_currency, exchange_rates_df):
        """
        Converte valor entre moedas usando as cotações

        Args:
            amount (float): Valor a ser convertido
            from_currency (str): Moeda de origem
            to_currency (str): Moeda de destino
            exchange_rates_df (pd.DataFrame): DataFrame com cotações

        Returns:
            float: Valor convertido
        """
        try:
            # Encontra a cotação da moeda de origem para USD
            from_rate_row = exchange_rates_df[exchange_rates_df['Moeda'] == from_currency]
            if from_rate_row.empty:
                logger.warning(f"Cotação não encontrada para {from_currency}")
                return amount

            from_rate = from_rate_row['Cotação'].iloc[0]

            # Encontra a cotação da moeda de destino para USD
            to_rate_row = exchange_rates_df[exchange_rates_df['Moeda'] == to_currency]
            if to_rate_row.empty:
                logger.warning(f"Cotação não encontrada para {to_currency}")
                return amount

            to_rate = to_rate_row['Cotação'].iloc[0]

            # Converte: valor_origem / taxa_origem * taxa_destino
            converted_amount = amount / from_rate * to_rate
            return converted_amount

        except Exception as e:
            logger.error(f"Erro na conversão de moeda: {e}")
            return amount

    def process_transactions(self, transactions_df, exchange_rates_df):
        """
        Processa as transações, convertendo valores para a moeda alvo

        Args:
            transactions_df (pd.DataFrame): DataFrame com transações
            exchange_rates_df (pd.DataFrame): DataFrame com cotações

        Returns:
            pd.DataFrame: DataFrame processado
        """
        try:
            # Cria uma cópia do DataFrame
            processed_df = transactions_df.copy()

            # Assume que há colunas 'Valor' e 'Moeda'
            if 'Valor' in processed_df.columns and 'Moeda' in processed_df.columns:
                # Converte os valores
                processed_df['Valor_Convertido'] = processed_df.apply(
                    lambda row: self.convert_currency(
                        row['Valor'],
                        row['Moeda'],
                        self.target_currency,
                        exchange_rates_df
                    ),
                    axis=1
                )

                # Adiciona coluna com a moeda alvo
                processed_df['Moeda_Alvo'] = self.target_currency

                logger.info("Transações processadas com sucesso")
            else:
                logger.warning("Colunas 'Valor' e/ou 'Moeda' não encontradas no DataFrame de transações")

            return processed_df

        except Exception as e:
            logger.error(f"Erro no processamento das transações: {e}")
            return transactions_df

    def generate_summary(self, processed_df):
        """
        Gera um resumo das transações processadas

        Args:
            processed_df (pd.DataFrame): DataFrame processado

        Returns:
            dict: Dicionário com estatísticas
        """
        try:
            summary = {}

            if 'Valor_Convertido' in processed_df.columns:
                summary['total_valor'] = processed_df['Valor_Convertido'].sum()
                summary['media_valor'] = processed_df['Valor_Convertido'].mean()
                summary['num_transacoes'] = len(processed_df)
                summary['moeda_alvo'] = self.target_currency

                # Calcula entradas e saídas
                if 'Tipo' in processed_df.columns:
                    income_mask = processed_df['Tipo'].str.contains('Recebimento|Investimento', case=False, na=False)
                    expense_mask = processed_df['Tipo'].str.contains('Compra|Pagamento|Transferência', case=False, na=False)

                    summary['total_income'] = processed_df.loc[income_mask, 'Valor_Convertido'].sum()
                    summary['total_expenses'] = processed_df.loc[expense_mask, 'Valor_Convertido'].sum()
                    summary['balance'] = summary['total_income'] - summary['total_expenses']

                    # Análise por categoria de despesa
                    summary['expenses_by_category'] = {}
                    for category in self.expense_categories:
                        category_mask = processed_df['Descrição'].str.contains(category, case=False, na=False) & expense_mask
                        summary['expenses_by_category'][category] = processed_df.loc[category_mask, 'Valor_Convertido'].sum()

                    # Detecta alertas (transações acima do threshold)
                    high_value_mask = processed_df['Valor_Convertido'] > self.alert_threshold
                    summary['alerts'] = len(processed_df[high_value_mask])
                    summary['alert_transactions'] = processed_df[high_value_mask][['Data', 'Descrição', 'Valor_Convertido']].to_dict('records')

            return summary

        except Exception as e:
            logger.error(f"Erro ao gerar resumo: {e}")
            return {}

    def process_all(self):
        """
        Método principal que executa todo o processamento

        Returns:
            tuple: (DataFrame processado, dicionário de resumo)
        """
        # Carrega os dados
        transactions_df = self.load_transactions()
        exchange_rates_df = self.load_exchange_rates()

        if transactions_df.empty or exchange_rates_df.empty:
            logger.error("Não foi possível carregar os dados necessários")
            return pd.DataFrame(), {}

        # Processa as transações
        processed_df = self.process_transactions(transactions_df, exchange_rates_df)

        # Gera resumo
        summary = self.generate_summary(processed_df)

        return processed_df, summary

if __name__ == "__main__":
    processor = DataProcessor()
    processed_data, summary = processor.process_all()
    print("Resumo do processamento:")
    print(summary)

# Função para uso direto (conforme esperado pelo main.py)
def process_transactions():
    """
    Função que processa as transações e retorna um resumo

    Returns:
        dict: Dicionário com resumo das transações
    """
    processor = DataProcessor()
    processed_data, summary = processor.process_all()

    if processed_data.empty:
        return {
            'total_transactions': 0,
            'total_income': 0.0,
            'total_expenses': 0.0,
            'balance': 0.0
        }

    # Retorna apenas os campos esperados pelo main.py
    return {
        'total_transactions': summary.get('num_transacoes', 0),
        'total_income': summary.get('total_income', 0.0),
        'total_expenses': summary.get('total_expenses', 0.0),
        'balance': summary.get('balance', 0.0)
    }

# Função para uso direto (conforme esperado pelo main.py)
def process_transactions():
    """
    Função que processa as transações e retorna um resumo

    Returns:
        dict: Dicionário com resumo das transações
    """
    processor = DataProcessor()
    processed_data, summary = processor.process_all()

    if processed_data.empty:
        return {
            'total_transactions': 0,
            'total_income': 0.0,
            'total_expenses': 0.0,
            'balance': 0.0
        }

    # Calcula totais baseado nos tipos de transação
    total_income = 0.0
    total_expenses = 0.0

    if 'Valor_Convertido' in processed_data.columns and 'Tipo' in processed_data.columns:
        income_mask = processed_data['Tipo'].str.contains('Recebimento|Investimento', case=False, na=False)
        expense_mask = processed_data['Tipo'].str.contains('Compra|Pagamento|Transferência', case=False, na=False)

        total_income = processed_data.loc[income_mask, 'Valor_Convertido'].sum()
        total_expenses = processed_data.loc[expense_mask, 'Valor_Convertido'].sum()

    balance = total_income - total_expenses

    return {
        'total_transactions': len(processed_data),
        'total_income': total_income,
        'total_expenses': total_expenses,
        'balance': balance
    }