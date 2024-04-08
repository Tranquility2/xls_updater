.PHONY: run clean

SHELL=/bin/bash

run:
	python3 xls_updater/app.py

setup:
	python3 -m pip install '.[dev, test, release]'

setup-dev:
	python3 -m pip install --editable '.[dev]'

setup-test:
	python3 -m pip install --editable '.[test]'

setup-relase:
	python3 -m pip install --editable '.[release]'

pip-clean:
	python3 -m pip uninstall -y -r <(pip freeze)

clean:
	rm -rf **/__pycache__ .pytest_cache/ dist/ .mypy_cache/ .coverage *.egg-info build

check-black:
	python3 -m black --diff --check .

check-isort:
	python3 -m isort --diff --check .

check-format: | check-black check-isort

fix-format:
	python3 -m black .
	python3 -m isort .

check-lint:
	python3 -m pylint --reports=True xls_updater

pytest:
	python3 -m pytest -v

coverage:
	python3 -m coverage run --source=xls_updater --module pytest \
	--verbose tests && coverage report --show-missing

tests: | pytest coverage

check-mypy:
	python3 -m mypy -p xls_updater

compile:
	python3 -m pip install --upgrade pip-tools
	python3 -m piptools compile -o requirements-dev.txt --extra dev pyproject.toml
	python3 -m piptools compile -o requirements-test.txt --extra test pyproject.toml
