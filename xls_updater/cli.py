"""Command line interface for xls_updater"""

import pathlib

import click

from xls_updater.app import convert_xls_to_xlsx


@click.command()
@click.argument("src_file_path", type=click.Path(exists=True, path_type=pathlib.Path))
@click.version_option()
def cli(src_file_path: pathlib.Path) -> None:
    """Convert an xls file to xlsx."""
    convert_xls_to_xlsx(src_file_path)
