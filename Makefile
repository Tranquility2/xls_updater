.PHONY: run clean

run:
	python xls_updater/app.py

setup:
	pip install .

setup-dev:
	pip install '.[dev]'

clean:
	rm -rf __pycache__
