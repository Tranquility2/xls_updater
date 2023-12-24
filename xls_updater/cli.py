"""Command line interface for xls_updater"""
import click

from xls_updater.app import convert_xls_to_xlsx


@click.command()
@click.argument("src_file_path", type=click.Path(exists=True))
@click.version_option()
def cli(src_file_path: str) -> None:
    """Wrapper for convert_xls_to_xlsx function"""
    convert_xls_to_xlsx(src_file_path)
