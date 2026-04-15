# Makefile for Bank Report Automator

.PHONY: help install test lint format clean build run

# Default target
help: ## Show this help message
	@echo "Bank Report Automator - Development Commands"
	@echo ""
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-15s %s\n", $$1, $$2}'

# Installation
install: ## Install all dependencies
	pip install -r requirements.txt

install-dev: ## Install development dependencies
	pip install -r requirements.txt
	pip install pytest pytest-cov flake8 black isort mypy bandit safety pre-commit

# Testing
test: ## Run all tests
	pytest

test-cov: ## Run tests with coverage
	pytest --cov=src --cov=main.py --cov-report=html --cov-report=term-missing

test-verbose: ## Run tests with verbose output
	pytest -v

# Code Quality
lint: ## Run all linting tools
	flake8 src/ main.py config.py
	black --check src/ main.py config.py
	isort --check-only src/ main.py config.py
	mypy src/ main.py config.py

format: ## Format code with black and isort
	black src/ main.py config.py
	isort src/ main.py config.py

security: ## Run security checks
	bandit -r src/ main.py config.py
	safety check

# Pre-commit
pre-commit-install: ## Install pre-commit hooks
	pre-commit install

pre-commit-run: ## Run pre-commit on all files
	pre-commit run --all-files

# Building
build: ## Build executable with PyInstaller
	pyinstaller --onefile --name bank-report-automator main.py

# Running
run: ## Run the application
	python main.py

# Cleaning
clean: ## Clean up generated files
	rm -rf dist/ build/ *.spec
	rm -rf htmlcov/ .coverage .coverage.*
	rm -rf __pycache__/ .pytest_cache/ .mypy_cache/
	rm -rf *.log

clean-all: clean ## Clean everything including venv
	rm -rf venv/ env/ .venv/

# Development setup
setup-dev: clean-all ## Set up development environment
	python -m venv venv
	venv\Scripts\activate && make install-dev
	pre-commit install

# CI simulation
ci: lint test security ## Run all CI checks locally