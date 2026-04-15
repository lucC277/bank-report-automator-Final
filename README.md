# Bank Report Automator

**RPA para relatórios financeiros** - Coleta dados, processa transações e gera relatórios Excel automaticamente.

## 🚀 Funcionalidades

- **📡 Coleta de Cotações**: Busca cotações USD/EUR via API do Banco Central do Brasil
- **📊 Processamento de Transações**: Converte valores para BRL e calcula estatísticas
- **⚠️ Sistema de Alertas**: Detecta transações acima do limite configurado (R$ 300,00)
- **📋 Relatórios Excel**: Gera relatório com múltiplas abas (dados, resumo, categorias, alertas)
- **📈 Análise por Categoria**: Classifica despesas em Alimentação, Transporte, Lazer, Saúde, Educação

## 📁 Estrutura do Projeto

```
bank-report-automator/
├── main.py                 # Script principal
├── config.py              # Configurações do projeto
├── data/
│   ├── transacoes.csv     # Dados de entrada das transações
│   └── cotacoes.xlsx      # Cotações coletadas automaticamente
├── reports/
│   └── relatorio_final.xlsx # Relatório Excel gerado
├── src/
│   ├── collector.py       # Coleta de cotações via API
│   ├── processor.py       # Processamento de dados
│   └── exporter.py        # Exportação para Excel
├── requirements.txt       # Dependências Python
├── README.md             # Esta documentação
└── .gitignore
```

## ⚙️ Configurações

As principais configurações estão em `config.py`:

- **APIs**: URLs do Banco Central para USD e EUR
- **Threshold de Alertas**: R$ 300,00 (padrão)
- **Mês do Relatório**: 2026-03
- **Categorias de Despesa**: Alimentação, Transporte, Lazer, Saúde, Educação

## 🛠️ Como Usar

1. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Prepare os dados**:
   - Adicione transações em `data/transacoes.csv`
   - Formato: Data,Descrição,Valor,Moeda,Tipo

3. **Execute o RPA**:
   ```bash
   python main.py
   ```

4. **Verifique o resultado**:
   - Relatório gerado em `reports/relatorio_final.xlsx`
   - Log de execução no console

## 📊 Exemplo de Saída

```
🏦 Bank Report Automator
========================
📡 Coletando cotações...
✅ USD: R$ 5.20 | EUR: R$ 6.10

📊 Processando transações de 2026-03...
✅ 10 transações processadas
   Entradas: R$ 15024.87
   Saídas:   R$ 10685.19
   Saldo:    R$ 4339.68

📋 Gerando relatório Excel...
✅ Relatório gerado com sucesso!

🎉 RPA concluído! Arquivo: reports/relatorio_final.xlsx
```

## 📈 Relatório Excel

O relatório contém as seguintes abas:

- **Relatório_Principal**: Dados processados completos
- **Resumo_Estatístico**: Métricas gerais e estatísticas
- **Despesas_por_Categoria**: Análise por categoria de despesa
- **Alertas**: Transações acima do threshold
- **Metadados**: Informações sobre a geração do relatório

## 🔧 Personalização

Para modificar configurações:

1. Edite `config.py` para alterar APIs, thresholds, etc.
2. Modifique `data/transacoes.csv` para adicionar novas transações
3. Ajuste as categorias em `config.py` conforme necessário

## 📋 Formato dos Dados

### transacoes.csv
```csv
Data,Descrição,Valor,Moeda,Tipo
2023-01-15,Compra online,150.00,USD,Compra
2023-01-16,Transferência internacional,500.00,EUR,Transferência
```

### Tipos de Transação
- **Compra**: Despesas gerais
- **Pagamento**: Contas e serviços
- **Transferência**: Movimentações bancárias
- **Recebimento**: Entradas de dinheiro
- **Investimento**: Aplicações financeiras

## 🤝 Contribuição

Para contribuir com o projeto:

1. Fork o repositório
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto é distribuído sob a licença MIT.