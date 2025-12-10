# Makefile

VENV := .venv
PYTHON := $(VENV)/bin/python
UV := uv

.PHONY: help init run lint typecheck format clean

help:
	@echo "Usage:"
	@echo "  make init         - Set up virtual environment and install dependencies"
	@echo "  make run          - Run FastAPI with Uvicorn (dev mode)"
	@echo "  make lint         - Run ruff linter"
	@echo "  make format       - Auto-format code with ruff"
	@echo "  make typecheck    - Run pyrefly type checker"
	@echo "  make clean        - Remove virtual environment"

dev_init:
	$(UV) init
	$(UV) venv $(VENV)
	$(UV) add -r requirements.txt
	$(UV) add --dev -r requirements.dev.txt

dev_requirements:
	$(UV) pip compile pyproject.toml -o requirements.txt

run:
	$(VENV)/bin/uvicorn app.main:app --reload

lint:
	$(VENV)/bin/ruff check .

format:
	$(VENV)/bin/ruff format .

typecheck:
	$(VENV)/bin/pyrefly check .

clean:
	rm -rf $(VENV)
