[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/) [![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint) [![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)

[![PyPI - Version](https://img.shields.io/pypi/v/xls-updater.svg?logo=pypi&label=PyPI&logoColor=gold)](https://pypi.org/project/xls-updater/) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/xls-updater.svg?logo=python&label=Python&logoColor=gold)](https://pypi.org/project/xls-updater/) [![Coverage Status](https://coveralls.io/repos/github/Tranquility2/xls_updater/badge.svg?branch=master)](https://coveralls.io/github/Tranquility2/xls_updater?branch=master) [![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

# xls_updater

Convert legacy xls data to newer xlsx format.

💭 [Based on the kind comment made by Jackypengyu](https://stackoverflow.com/a/39461816 "Link")

## Install
### PIP
```bash
pip install xls-updater
```

### Binary
A binary version of this tool is available for download:  
```bash
wget https://github.com/Tranquility2/xls_updater/releases/latest/download/xls_updater
chmod +x xls_updater
```
Hashes are available for verification:  
[md5](https://github.com/Tranquility2/xls_updater/releases/latest/download/xls_updater.md5)  
[sha2256](https://github.com/Tranquility2/xls_updater/releases/latest/download/xls_updater.sha256)

## Usage

```
Usage: python -m xls_updater [OPTIONS] SRC_FILE_PATH

  Convert an xls file to xlsx.

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.
```

## Development

Please see [CONTRIBUTING.md](https://github.com/Tranquility2/xls_updater/blob/master/CONTRIBUTING.md)

## License

This project is published under the MIT license.

If you do find it useful, please consider contributing your changes back upstream.
