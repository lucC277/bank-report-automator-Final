"""
Tests for the processor module
"""
import pytest
import pandas as pd
from unittest.mock import patch, MagicMock
from src.processor import DataProcessor, process_transactions


class TestDataProcessor:
    """Test cases for DataProcessor class"""

    def test_init(self):
        """Test processor initialization"""
        processor = DataProcessor()
        assert processor.transactions_file is not None
        assert processor.exchange_rates_file is not None
        assert processor.target_currency == "BRL"
        assert processor.alert_threshold == 300.00

    def test_load_transactions_success(self):
        """Test successful transaction loading"""
        sample_data = {
            'Data': ['2023-01-01', '2023-01-02'],
            'Descrição': ['Test 1', 'Test 2'],
            'Valor': [100.0, 200.0],
            'Moeda': ['USD', 'EUR'],
            'Tipo': ['Compra', 'Recebimento']
        }
        df = pd.DataFrame(sample_data)

        with patch('pandas.read_csv', return_value=df):
            processor = DataProcessor()
            result = processor.load_transactions()

            assert len(result) == 2
            assert result['Valor'].iloc[0] == 100.0

    def test_load_transactions_error(self):
        """Test transaction loading error handling"""
        with patch('pandas.read_csv', side_effect=Exception("File not found")):
            processor = DataProcessor()
            result = processor.load_transactions()

            assert result.empty

    def test_convert_currency(self):
        """Test currency conversion"""
        sample_rates = pd.DataFrame({
            'Moeda': ['USD', 'EUR'],
            'Cotação': [5.20, 6.10],
            'Data': ['2024-01-01', '2024-01-01']
        })

        processor = DataProcessor()
        result = processor.convert_currency(100, 'USD', 'EUR', sample_rates)

        # Expected: 100 / 5.20 * 6.10 = 117.31
        assert abs(result - 117.31) < 0.01

    def test_generate_summary(self):
        """Test summary generation"""
        sample_data = pd.DataFrame({
            'Valor_Convertido': [1000, 2000, 500],
            'Tipo': ['Recebimento', 'Recebimento', 'Compra'],
            'Descrição': ['Salário', 'Freelance', 'Alimentação'],
            'Data': ['2024-01-01', '2024-01-02', '2024-01-03']
        })

        processor = DataProcessor()
        summary = processor.generate_summary(sample_data)

        assert summary['total_income'] == 3000
        assert summary['total_expenses'] == 500
        assert summary['balance'] == 2500
        assert summary['num_transacoes'] == 3
        assert summary['total_income'] == 3000  # 1000 + 2000
        assert summary['total_expenses'] == 500  # 500
        assert summary['balance'] == 2500  # 3000 - 500

    @patch('src.processor.DataProcessor.load_transactions')
    @patch('src.processor.DataProcessor.load_exchange_rates')
    def test_process_all_success(self, mock_load_rates, mock_load_transactions):
        """Test successful processing of all data"""
        # Mock transaction data
        transactions = pd.DataFrame({
            'Data': ['2023-01-01'],
            'Descrição': ['Test'],
            'Valor': [100.0],
            'Moeda': ['USD'],
            'Tipo': ['Compra']
        })

        # Mock exchange rates
        rates = pd.DataFrame({
            'Moeda': ['USD'],
            'Cotação': [5.20],
            'Data': ['2024-01-01']
        })

        mock_load_transactions.return_value = transactions
        mock_load_rates.return_value = rates

        processor = DataProcessor()
        processed_data, summary = processor.process_all()

        assert not processed_data.empty
        assert 'Valor_Convertido' in processed_data.columns
        assert summary['num_transacoes'] == 1

    def test_process_transactions_function(self):
        """Test the process_transactions function"""
        with patch('src.processor.DataProcessor.process_all') as mock_process:
            mock_process.return_value = (pd.DataFrame(), {'num_transacoes': 0})

            result = process_transactions()

            assert result['total_transactions'] == 0
            assert result['total_income'] == 0.0
            assert result['total_expenses'] == 0.0
            assert result['balance'] == 0.0