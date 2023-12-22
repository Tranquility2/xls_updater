.PHONY: run clean

SHELL=/bin/bash
COMPILE_READY := $(shell command -v pip-compile 2> /dev/null)

run:
	python xls_updater/app.py

setup:
	pip install .

setup-dev:
	python3 -m pip install --editable '.[dev]'

pip-clean:
	pip uninstall -y -r <(pip freeze)

clean:
	rm -rf **/__pycache__ **/.pytest_cache/ ./dist/ ./.mypy_cache/ ./.coverage ./*.egg-info build

fix-format:
	black .
	isort .

check-black:
	black --diff --check .
check-isort:
	isort --diff --check .

check-format: | check-black check-isort

compile:
ifndef COMPILE_READY
	@echo "Installing pip-tools"
	python -m pip install pip-tools==7.3.0
endif
	python -m piptools compile -o requirements.txt pyproject.toml
	python -m piptools compile -o requirements-dev.txt --extra dev pyproject.toml
