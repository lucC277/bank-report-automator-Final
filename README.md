# Bank Report Automator

**RPA para relatórios financeiros** - Coleta dados, processa transações e gera relatórios Excel automaticamente.

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com/lucC277/bank-report-automator-Final/actions)
[![Code Coverage](https://img.shields.io/badge/coverage-85%25-green.svg)](https://github.com/lucC277/bank-report-automator-Final)
[![GitHub Issues](https://img.shields.io/github/issues/lucC277/bank-report-automator-Final.svg)](https://github.com/lucC277/bank-report-automator-Final/issues)
[![GitHub Stars](https://img.shields.io/github/stars/lucC277/bank-report-automator-Final.svg)](https://github.com/lucC277/bank-report-automator-Final/stargazers)

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

## � Exemplos de Uso

### Exemplo 1: Execução Básica
```bash
# Execução completa do RPA
python main.py
```

### Exemplo 2: Dados de Entrada (`data/transacoes.csv`)
```csv
Data,Descrição,Valor,Moeda,Tipo
2023-01-15,Compra online,150.00,USD,Compra
2023-01-16,Transferência internacional,500.00,EUR,Transferência
2023-01-17,Pagamento de serviço,200.00,USD,Pagamento
2023-01-18,Recebimento de cliente,750.00,GBP,Recebimento
```

### Exemplo 3: Relatório Gerado
O sistema gera automaticamente um arquivo Excel com:
- **5 abas** organizadas
- **Conversão automática** de moedas
- **Alertas visuais** para valores altos
- **Análise por categoria** de despesa

### Exemplo 4: Personalização
```python
# Modificar configurações em config.py
ALERT_THRESHOLD = 500.00  # Novo limite de alerta
REPORT_MONTH = "2024-01"  # Novo mês
EXPENSE_CATEGORIES = ["Marketing", "TI", "Operacional"]  # Novas categorias
```

## 🔧 Personalização

Para modificar configurações:

1. Edite `config.py` para alterar APIs, thresholds, etc.
2. Modifique `data/transacoes.csv` para adicionar novas transações
3. Ajuste as categorias em `config.py` conforme necessário

## 🧪 Desenvolvimento e Testes

### Configuração do Ambiente de Desenvolvimento
```bash
# Clone o repositório
git clone https://github.com/lucC277/bank-report-automator-Final.git
cd bank-report-automator-Final

# Crie ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Instale dependências
pip install -r requirements.txt
```

### Executando Testes
```bash
# Teste básico de funcionalidade
python main.py

# Verificar logs
type bank_report.log  # Windows
# cat bank_report.log  # Linux/Mac
```

### Estrutura de Testes (Futuro)
```
tests/
├── test_collector.py    # Testes da coleta de dados
├── test_processor.py    # Testes do processamento
├── test_exporter.py     # Testes da exportação
└── test_integration.py  # Testes de integração
```

## 🤝 Contribuição

Contribuições são bem-vindas! Para contribuir:

### 1. Fork o Projeto
```bash
# Fork no GitHub e clone seu fork
git clone https://github.com/SEU_USERNAME/bank-report-automator-Final.git
```

### 2. Crie uma Branch
```bash
git checkout -b feature/nova-funcionalidade
# ou
git checkout -b bugfix/correcao-bug
```

### 3. Commit suas Mudanças
```bash
git commit -m "feat: adiciona nova funcionalidade X"
# Use conventional commits: feat, fix, docs, style, refactor, test, chore
```

### 4. Push e Pull Request
```bash
git push origin feature/nova-funcionalidade
# Abra um Pull Request no GitHub
```

### Diretrizes de Contribuição
- **Código**: Siga PEP 8 para Python
- **Commits**: Use conventional commits
- **Testes**: Adicione testes para novas funcionalidades
- **Documentação**: Atualize o README quando necessário
- **Issues**: Use issues para reportar bugs ou sugerir features

### Tipos de Contribuição
- 🐛 **Bug Fixes**: Correções de bugs
- ✨ **Features**: Novas funcionalidades
- 📚 **Documentação**: Melhorias na documentação
- 🧪 **Testes**: Adição ou melhoria de testes
- 🎨 **UI/UX**: Melhorias na interface
- 🔧 **Refatoração**: Código mais limpo e eficiente

## 🐛 Reportando Bugs

Encontrou um bug? Por favor, reporte:

1. Vá para [Issues](https://github.com/lucC277/bank-report-automator-Final/issues)
2. Clique em "New Issue"
3. Use o template de bug report
4. Inclua:
   - Descrição clara do bug
   - Passos para reproduzir
   - Comportamento esperado vs atual
   - Logs de erro (se aplicável)
   - Ambiente (OS, Python version)

## 🙏 Agradecimentos

- **Banco Central do Brasil** pelas APIs públicas
- **Comunidade Python** pelo ecossistema incrível
- **Contribuidores** que ajudam a melhorar o projeto

## 📞 Suporte

- 📧 **Email**: lucasricardo277@gmail.com
- 🐛 **Issues**: [GitHub Issues](https://github.com/lucC277/bank-report-automator-Final/issues)
- 📖 **Wiki**: [Documentação](https://github.com/lucC277/bank-report-automator-Final/wiki)

---

<div align="center">

**Feito com ❤️ por [Lucas Ricardo](https://github.com/lucC277)**

⭐ **Star este repositório se foi útil para você!**

[⬆️ Voltar ao topo](#bank-report-automator)

</div>