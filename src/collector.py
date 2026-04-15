# collector.py - Módulo para coleta de dados de cotações

import requests
import pandas as pd
from datetime import datetime, timedelta
import logging
from config import USD_API_URL, EUR_API_URL, EXCHANGE_RATES_FILE, DEFAULT_CURRENCY

# Configuração do logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ExchangeRateCollector:
    def __init__(self):
        self.usd_api_url = USD_API_URL
        self.eur_api_url = EUR_API_URL
        self.default_currency = DEFAULT_CURRENCY

    def get_exchange_rates(self, base_currency=None, date=None):
        """
        Coleta cotações de moedas das APIs do Banco Central do Brasil

        Args:
            base_currency (str): Moeda base (padrão: USD)
            date (str): Data específica no formato YYYY-MM-DD

        Returns:
            dict: Dicionário com as cotações
        """
        try:
            rates = {}

            # Busca cotação do USD
            usd_response = requests.get(self.usd_api_url)
            usd_response.raise_for_status()
            usd_data = usd_response.json()

            if usd_data:
                # Pega o último valor disponível
                latest_usd = usd_data[-1]
                rates['USD'] = float(latest_usd.get('valor', 0))
                logger.info(f"Cotação USD obtida: R$ {rates['USD']}")

            # Busca cotação do EUR
            eur_response = requests.get(self.eur_api_url)
            eur_response.raise_for_status()
            eur_data = eur_response.json()

            if eur_data:
                # Pega o último valor disponível
                latest_eur = eur_data[-1]
                rates['EUR'] = float(latest_eur.get('valor', 0))
                logger.info(f"Cotação EUR obtida: R$ {rates['EUR']}")

            return rates

        except requests.RequestException as e:
            logger.error(f"Erro ao coletar cotações: {e}")
            return {}
        except (ValueError, KeyError) as e:
            logger.error(f"Erro ao processar dados da API: {e}")
            return {}

    def save_exchange_rates_to_excel(self, rates, filename=None):
        """
        Salva as cotações em um arquivo Excel

        Args:
            rates (dict): Dicionário com as cotações
            filename (str): Nome do arquivo (padrão: config.EXCHANGE_RATES_FILE)
        """
        if filename is None:
            filename = EXCHANGE_RATES_FILE

        try:
            # Converte para DataFrame
            df = pd.DataFrame(list(rates.items()), columns=['Moeda', 'Cotação'])
            df['Data'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Salva em Excel
            with pd.ExcelWriter(filename, engine='openpyxl') as writer:
                df.to_excel(writer, sheet_name='Cotações', index=False)

            logger.info(f"Cotações salvas em {filename}")

        except Exception as e:
            logger.error(f"Erro ao salvar cotações: {e}")

    def collect_and_save_rates(self, base_currency=None):
        """
        Coleta e salva as cotações automaticamente
        """
        rates = self.get_exchange_rates(base_currency)
        if rates:
            self.save_exchange_rates_to_excel(rates)
            return True
        return False

if __name__ == "__main__":
    collector = ExchangeRateCollector()
    collector.collect_and_save_rates()

# Função para uso direto (conforme esperado pelo main.py)
def collect_exchange_rates():
    """Coleta cotações do dólar e euro via API do Bacen"""
    rates = {}

    # Dólar
    try:
        response = requests.get(USD_API_URL)
        if response.status_code == 200:
            data = response.json()
            df_usd = pd.DataFrame(data)
            df_usd["data"] = pd.to_datetime(df_usd["data"], format="%d/%m/%Y")
            df_usd["valor"] = df_usd["valor"].astype(float)
            rates["USD"] = df_usd.iloc[-1]["valor"]
    except Exception as e:
        print(f"Erro coletando USD: {e}")

    # Euro
    try:
        response = requests.get(EUR_API_URL)
        if response.status_code == 200:
            data = response.json()
            df_eur = pd.DataFrame(data)
            df_eur["data"] = pd.to_datetime(df_eur["data"], format="%d/%m/%Y")
            df_eur["valor"] = df_eur["valor"].astype(float)
            rates["EUR"] = df_eur.iloc[-1]["valor"]
    except Exception as e:
        print(f"Erro coletando EUR: {e}")

    # Salvar histórico
    if rates:
        df_final = pd.DataFrame(list(rates.items()), columns=["moeda", "valor"])
        df_final["data_coleta"] = datetime.now()
        df_final.to_excel(EXCHANGE_RATES_FILE, index=False)

    return rates
    return {'USD': 5.20, 'EUR': 6.10}