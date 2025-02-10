SHELL=/bin/bash
VENV:=./.venv
BIN := $(VENV)/bin
PIP := $(BIN)/pip
PYTHON:=$(BIN)/python3

.venv:
	python3 -m venv $@

install: .venv
	$(PIP) install -r requirements.txt

start:
	$(PYTHON) -m amok