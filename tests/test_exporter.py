"""
Tests for the exporter module
"""
import pytest
import pandas as pd
from unittest.mock import patch, MagicMock
import os
from src.exporter import DataExporter, export_report


class TestDataExporter:
    """Test cases for DataExporter class"""

    def test_init(self):
        """Test exporter initialization"""
        exporter = DataExporter()
        assert exporter.final_report_file is not None
        assert exporter.expense_categories is not None
        assert exporter.alert_threshold == 300.00

    @patch('pandas.DataFrame.to_excel')
    def test_export_to_excel(self, mock_to_excel):
        """Test Excel export functionality"""
        sample_data = pd.DataFrame({
            'Data': ['2023-01-01'],
            'Descrição': ['Test'],
            'Valor': [100.0]
        })

        sample_summary = {
            'total_valor': 100.0,
            'num_transacoes': 1
        }

        exporter = DataExporter()
        exporter.export_to_excel(sample_data, sample_summary)

        # Verify that to_excel was called
        assert mock_to_excel.called

    @patch('src.exporter.DataExporter.create_formatted_report')
    def test_export_report_function(self, mock_create_report):
        """Test the export_report function"""
        sample_summary = {
            'total_transactions': 10,
            'total_income': 1000.0,
            'total_expenses': 500.0,
            'balance': 500.0
        }

        sample_rates = {'USD': 5.20, 'EUR': 6.10}

        export_report(sample_summary, sample_rates)

        # Verify that create_formatted_report was called
        assert mock_create_report.called

    @patch('pandas.DataFrame.to_excel')
    def test_create_formatted_report(self, mock_to_excel):
        """Test creation of formatted report"""
        sample_data = pd.DataFrame({
            'Data': ['2023-01-01'],
            'Descrição': ['Test transaction'],
            'Valor': [100.0],
            'Moeda': ['USD'],
            'Valor_Convertido': [520.0],
            'Tipo': ['Compra']
        })

        sample_summary = {
            'total_valor': 520.0,
            'num_transacoes': 1,
            'total_income': 0.0,
            'total_expenses': 520.0,
            'balance': -520.0,
            'expenses_by_category': {'Alimentação': 0.0},
            'alerts': 0
        }

        exporter = DataExporter()
        exporter.create_formatted_report(sample_data, sample_summary)

        # Verify that to_excel was called multiple times (for different sheets)
        assert mock_to_excel.call_count >= 3  # At least 3 sheets: principal, resumo, metadados