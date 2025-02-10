SHELL=/bin/bash
VENV:=./.venv
BIN := $(VENV)/bin
PIP := $(BIN)/pip

.venv:
	python3 -m venv $@

install: .venv
	$(PIP) install -r requirements.txt