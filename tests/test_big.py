""" Test using a very big generated xls file """

from pathlib import Path

import openpyxl
import xlrd
import xlwt

from xls_updater.app import convert_xls_to_xlsx


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

    print(f"big.xls size: {Path('big.xls').stat().st_size / 1024:.2f} KB")
    print(f"big.xlsx size: {Path('big.xlsx').stat().st_size / 1024:.2f} KB")
    Path("big.xls").unlink()
    Path("big.xlsx").unlink()
