""" Test using a very big generated xls file """

from pathlib import Path
from typing import List

import humanize
import openpyxl
import xlrd
import xlwt

from xls_updater.app import convert_xls_to_xlsx


def file_size_str(file_path: Path) -> str:
    """Return the file size as a string"""
    return humanize.naturalsize(file_path.stat().st_size)


def print_files_table(file_list: List[Path]) -> None:
    """Print a table with the file names and sizes"""
    max_name_len = max(len(file_path.name) for file_path in file_list)
    total_line_len = max_name_len + 3 + 10
    print("-" * total_line_len)
    for file_path in file_list:
        print(f"{file_path.name:<10} | {file_size_str(file_path)}")
    print("-" * total_line_len)


def generate_big_xls_file(file_name: str, factor: int = 16) -> None:
    """Generate a big xls file"""
    book = xlwt.Workbook()
    for s in range(factor):
        sheet = book.add_sheet(f"Sheet{s}")
        for i in range(factor * 256):
            for j in range(factor * 16):
                sheet.write(i, j, i * j)
    book.save(file_name)


def test_big_xls_file() -> None:
    """Test using a very big generated xls file"""
    generate_big_xls_file(file_name="big.xls", factor=4)
    convert_xls_to_xlsx(Path("big.xls"))
    assert Path("big.xlsx").exists()
    # check content
    book_xlsx = openpyxl.load_workbook("big.xlsx")
    book_xls = xlrd.open_workbook("big.xls")
    for sheet_xlsx, sheet_xls in zip(book_xlsx, book_xls):
        for row_xlsx, row_xls in zip(sheet_xlsx, sheet_xls):
            for cell_xlsx, cell_xls in zip(row_xlsx, row_xls):
                assert cell_xlsx.value == cell_xls.value

    print_files_table([Path("big.xls"), Path("big.xlsx")])

    Path("big.xls").unlink()
    Path("big.xlsx").unlink()
