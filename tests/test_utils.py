"""Test utils module."""
from xls_updater.utils import change_file_extension_with_string_methods


def test_change_file_extension_with_string_methods():
    """Test change_file_extension_with_string_methods."""
    filename = "test_file.txt"
    new_extension = "csv"
    new_filename = change_file_extension_with_string_methods(filename, new_extension)
    assert new_filename == "test_file.csv"


def test_change_file_extension_with_string_methods_no_dot():
    """Test change_file_extension_with_string_methods."""
    filename = "test_file"
    new_extension = "txt"
    new_filename = change_file_extension_with_string_methods(filename, new_extension)
    assert new_filename == "test_file.txt"
