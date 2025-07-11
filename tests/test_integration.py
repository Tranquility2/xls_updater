"""Integration tests for the xls_updater package."""

import subprocess
import tempfile
from typing import Optional, Tuple

from pytest import fixture


class RunCommandException(Exception):
    """Exception raised when a command fails."""

    def __init__(self, message: str) -> None:
        """Initialize the exception."""
        super().__init__(message)


def run_command(command: str, cwd: str, validation_string: Optional[str] = None) -> Tuple[str, str]:
    """Run a command in a subprocess and return the output. Raise an exception if the command fails."""
    result = subprocess.run(command, capture_output=True, shell=True, text=True, check=False, cwd=cwd)
    if result.returncode != 0:
        print(f"Error running command {command} in {cwd}")
        raise RunCommandException(f"Error {result.stderr}, Code: {result.returncode}, Command output: {result.stdout}")
    if validation_string:
        print(f"[v] {validation_string}")
    return (result.stdout, result.stderr)


class TestIntegration:
    """Integration tests for the xls_updater package."""

    @fixture(autouse=True)
    def get_available_files(self) -> None:
        """Get the available files in the temporary directory."""
        file_names_str, _ = run_command("ls", self.tmpdirname, "Get available files")
        file_names_list = file_names_str.split()
        self.avilable_files = file_names_list  # pylint: disable=attribute-defined-outside-init

    def setup_method(self) -> None:
        """Create a temporary directory."""
        self.tmpdirname = tempfile.mkdtemp()  # pylint: disable=attribute-defined-outside-init
        print()  # Add a newline for readability
        run_command(f"cp tests/samples/*.xls {self.tmpdirname}", ".", "Copy test data")

    def teardown_method(self) -> None:
        """Remove the temporary directory."""
        run_command(f"rm -rf {self.tmpdirname}", self.tmpdirname)

    def test_sanity(self) -> None:
        """Test that the test runner is working."""
        print(f"Files in {self.tmpdirname}:\n{self.avilable_files}")
        assert any("sample" in f for f in self.avilable_files)

    def test_version(self) -> None:
        """Test that the version command works."""
        result, _ = run_command("xls-updater --version", self.tmpdirname, "Print Version")
        assert "xls-updater" in result
        assert "version" in result

    def test_help(self) -> None:
        """Test that the help command works."""
        result, _ = run_command("xls-updater --help", self.tmpdirname, "Print Help")
        assert "xls-updater" in result
        assert "help" in result

    def test_update(self) -> None:
        """Test that the update command works."""
        for file_name in self.avilable_files:
            _, log = run_command(f"xls-updater {file_name}", self.tmpdirname, f"Update file {file_name}")
            print(log)

        file_names, _ = run_command("ls", self.tmpdirname, "Get updated files")
        for file_name in self.avilable_files:
            new_file_name = file_name.replace("xls", "xlsx")
            assert new_file_name in file_names

        print(f"Files in {self.tmpdirname}:\n{file_names.split()}")
