"""
Tests for the collector module
"""
import pytest
from unittest.mock import patch, MagicMock
import pandas as pd
from src.collector import ExchangeRateCollector, collect_exchange_rates


class TestExchangeRateCollector:
    """Test cases for ExchangeRateCollector class"""

    def test_init(self):
        """Test collector initialization"""
        collector = ExchangeRateCollector()
        assert collector.usd_api_url is not None
        assert collector.eur_api_url is not None
        assert collector.default_currency == "USD"

    @patch('src.collector.requests.get')
    def test_get_exchange_rates_success(self, mock_get):
        """Test successful exchange rate collection"""
        # Mock API responses
        mock_usd_response = MagicMock()
        mock_usd_response.status_code = 200
        mock_usd_response.json.return_value = [
            {"data": "01/01/2024", "valor": "5.20"}
        ]

        mock_eur_response = MagicMock()
        mock_eur_response.status_code = 200
        mock_eur_response.json.return_value = [
            {"data": "01/01/2024", "valor": "6.10"}
        ]

        mock_get.side_effect = [mock_usd_response, mock_eur_response]

        collector = ExchangeRateCollector()
        rates = collector.get_exchange_rates()

        assert rates['USD'] == 5.20
        assert rates['EUR'] == 6.10
        assert mock_get.call_count == 2

    @patch('src.collector.requests.get')
    def test_get_exchange_rates_api_error(self, mock_get):
        """Test handling of API errors"""
        from requests import RequestException
        mock_get.side_effect = RequestException("API Error")

        collector = ExchangeRateCollector()
        rates = collector.get_exchange_rates()

        assert rates == {}

    @patch('src.collector.requests.get')
    def test_collect_exchange_rates_function(self, mock_get):
        """Test the collect_exchange_rates function"""
        # Mock successful API responses
        mock_usd_response = MagicMock()
        mock_usd_response.status_code = 200
        mock_usd_response.json.return_value = [
            {"data": "01/01/2024", "valor": "5.20"}
        ]

        mock_eur_response = MagicMock()
        mock_eur_response.status_code = 200
        mock_eur_response.json.return_value = [
            {"data": "01/01/2024", "valor": "6.10"}
        ]

        mock_get.side_effect = [mock_usd_response, mock_eur_response]

        rates = collect_exchange_rates()

        assert rates['USD'] == 5.20
        assert rates['EUR'] == 6.10