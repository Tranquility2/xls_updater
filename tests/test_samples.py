""" Test that all sample files are converted to xlsx correctly """

from pathlib import Path
from typing import List

import openpyxl
import pandas as pd

from xls_updater.app import convert_xls_to_xlsx

SAMPLES_SOURCE_DIR = Path("tests/samples")


def genrate_sample_files_list(sample_dir: Path) -> List[Path]:
    """Generate list of sample files from sample directory"""
    return list(sample_dir.glob("*.xls"))


def convert_sample_files(sample_files: List[Path]) -> List[Path]:
    """Convert sample files to xlsx and return list of converted files"""
    for sample_file in sample_files:
        convert_xls_to_xlsx(Path(sample_file))

    # generate list of converted files
    converted_files = [f.with_suffix(".xlsx") for f in sample_files]
    return converted_files


def test_convert_xls_to_xlsx() -> None:
    """Test that all sample files are converted to xlsx correctly"""
    sample_files = genrate_sample_files_list(SAMPLES_SOURCE_DIR)
    converted_sample_files = convert_sample_files(sample_files)

    # check that all files were converted
    for sample_file in converted_sample_files:
        assert sample_file.exists()

    # check that all files are valid xlsx with assert
    for sample_file in converted_sample_files:
        assert openpyxl.load_workbook(sample_file)

    sample_files_str = [str(f) for f in sample_files]
    converted_sample_files_str = [str(f) for f in converted_sample_files]

    for orignal, new in zip(sample_files_str, converted_sample_files_str):
        orignal_data = pd.read_excel(orignal)
        convereted_data = pd.read_excel(new)
        assert orignal_data.equals(convereted_data)

    # Cleanup
    for sample_file in sample_files:
        sample_file.with_suffix(".xlsx").unlink()
