"""Command line interface for xls_updater"""

import pathlib

import click

from xls_updater.__about__ import __version__
from xls_updater.app import convert_xls_to_xlsx


@click.group(invoke_without_command=True, no_args_is_help=True)
@click.version_option(__version__, "-v", "--version", is_flag=True, help="Show the version.")
@click.argument("src_file_path", type=click.Path(exists=True, path_type=pathlib.Path), required=True)
def cli(src_file_path: pathlib.Path) -> None:
    """Convert an xls file to xlsx."""
    convert_xls_to_xlsx(src_file_path)
