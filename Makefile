.PHONY: run clean

SHELL=/bin/bash

run:
	python xls_updater/app.py

setup:
	pip install .

setup-dev:
	python3 -m pip install --editable '.[dev]'

pip-clean:
	pip uninstall -y -r <(pip freeze)

clean:
	rm -rf **/__pycache__ .pytest_cache/ dist/ .mypy_cache/ .coverage *.egg-info build

check-black:
	black --diff --check .

check-isort:
	isort --diff --check .

check-format: | check-black check-isort

fix-format:
	black .
	isort .

lint:
	pylint --reports=True xls_updater

pytest:
	python3 -m pytest -v

coverage:
	coverage run --source=xls_updater --module pytest \
	--verbose tests && coverage report --show-missing

tests: | pytest coverage

mypy:
	mypy -p xls_updater

compile:
	pip install --upgrade pip-tools
	python -m piptools compile -o requirements.txt pyproject.toml
	python -m piptools compile -o requirements-dev.txt --extra dev pyproject.toml

build:
	pip install --upgrade build
	python -m build
