.PHONY: run clean

SHELL=/bin/bash
COMPILE_READY := $(shell command -v pip-compile 2> /dev/null)

run:
	python xls_updater/app.py

setup:
	pip install .

setup-dev:
	pip install '.[dev]'

pip-clean:
	pip uninstall -y -r <(pip freeze)

clean:
	rm -rf __pycache__

compile:
ifndef COMPILE_READY
	@echo "Installing pip-tools"
	python -m pip install pip-tools==7.3.0
endif
	python -m piptools compile -o requirements.txt pyproject.toml
	python -m piptools compile -o requirements-dev.txt --extra dev pyproject.toml
