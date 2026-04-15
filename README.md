# Bank Report Automator

**RPA para relatórios financeiros** - Coleta dados, processa transações e gera relatórios Excel automaticamente.

[![CI/CD Pipeline](https://github.com/lucC277/bank-report-automator-Final/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/lucC277/bank-report-automator-Final/actions)
[![Code Coverage](https://codecov.io/gh/lucC277/bank-report-automator-Final/branch/master/graph/badge.svg)](https://codecov.io/gh/lucC277/bank-report-automator-Final)
[![Python Versions](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Quality](https://img.shields.io/badge/code%20quality-A-green)](https://github.com/lucC277/bank-report-automator-Final)
[![Security](https://img.shields.io/badge/security-checked-green)](https://github.com/lucC277/bank-report-automator-Final)

## 🚀 Funcionalidades

- **📡 Coleta de Cotações**: Busca cotações USD/EUR via API do Banco Central do Brasil
- **📊 Processamento de Transações**: Converte valores para BRL e calcula estatísticas
- **⚠️ Sistema de Alertas**: Detecta transações acima do limite configurado (R$ 300,00)
- **📋 Relatórios Excel**: Gera relatório com múltiplas abas (dados, resumo, categorias, alertas)
- **📈 Análise por Categoria**: Classifica despesas em Alimentação, Transporte, Lazer, Saúde, Educação

## � Monitoramento e Qualidade

### Status do CI/CD
O projeto utiliza GitHub Actions para garantia de qualidade automática:

- **✅ CI/CD Pipeline**: [Ver status](https://github.com/lucC277/bank-report-automator-Final/actions)
- **📊 Cobertura de Código**: [Ver relatório](https://codecov.io/gh/lucC277/bank-report-automator-Final)
- **🔒 Segurança**: Verificações automáticas com Bandit e Safety
- **🎯 Qualidade**: Linting, formatação e testes em múltiplas versões Python

### Métricas Atuais
- **Testes**: 15/15 passando
- **Cobertura**: >80% alvo mínimo
- **Python**: 3.8, 3.9, 3.10, 3.11, 3.12
- **Segurança**: Verificada automaticamente

## �📁 Estrutura do Projeto

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

## 🚀 CI/CD e Desenvolvimento

### Pipeline de CI/CD
O projeto utiliza GitHub Actions para automação completa:

- **✅ Testes Automatizados**: pytest com cobertura de código
- **🔍 Linting e Formatação**: flake8, black, isort, mypy
- **🔒 Segurança**: bandit e safety para vulnerabilidades
- **📦 Build**: Geração de executáveis com PyInstaller
- **📊 Cobertura**: Relatórios de cobertura via Codecov

### Status do Pipeline
[![CI/CD Pipeline](https://github.com/lucC277/bank-report-automator-Final/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/lucC277/bank-report-automator-Final/actions)
[![Code Coverage](https://codecov.io/gh/lucC277/bank-report-automator-Final/branch/master/graph/badge.svg)](https://codecov.io/gh/lucC277/bank-report-automator-Final)

### Ferramentas de Desenvolvimento

#### Instalação Completa para Desenvolvimento
```bash
# Instale dependências de desenvolvimento
pip install -r requirements-dev.txt

# Configure pre-commit hooks
pre-commit install

# Execute todos os testes
make test

# Execute linting completo
make lint

# Formate o código
make format
```

#### Comandos Disponíveis (Makefile)
```bash
make help          # Mostra todos os comandos disponíveis
make test          # Executa testes com pytest
make test-cov      # Executa testes com relatório de cobertura
make lint          # Executa flake8, black, isort, mypy
make format        # Formata código com black e isort
make security      # Executa verificações de segurança
make build         # Gera executável com PyInstaller
make clean         # Limpa arquivos temporários
make dev-setup     # Configura ambiente de desenvolvimento
```

#### Estrutura de Testes
```
tests/
├── test_collector.py    # Testes para coleta de cotações
├── test_processor.py    # Testes para processamento de dados
└── test_exporter.py     # Testes para exportação Excel
```

#### Configurações de Qualidade de Código
- **black**: Formatação automática de código
- **isort**: Organização de imports
- **flake8**: Linting e detecção de problemas
- **mypy**: Verificação de tipos estáticos
- **bandit**: Análise de segurança
- **safety**: Verificação de vulnerabilidades em dependências

### Contribuição
1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Execute os testes e linting (`make test && make lint`)
4. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
5. Push para a branch (`git push origin feature/nova-funcionalidade`)
6. Abra um Pull Request

### Pré-commit Hooks
O projeto utiliza pre-commit para automatizar verificações antes de cada commit:
- Formatação de código
- Linting
- Verificação de tipos
- Testes rápidos

##  Contribuição

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