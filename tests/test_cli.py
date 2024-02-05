"""Test app."""

from pathlib import Path
from unittest.mock import MagicMock

from click.testing import CliRunner
from pytest import fixture
from pytest_mock import MockerFixture

from xls_updater.cli import cli


@fixture(name="convert_xls_to_xlsx")
def mock_convert_xls_to_xlsx(mocker: MockerFixture) -> MagicMock:
    """Mock convert_xls_to_xlsx."""
    return mocker.patch("xls_updater.cli.convert_xls_to_xlsx")


def test_cli(convert_xls_to_xlsx: MagicMock) -> None:
    """Test app."""
    runner = CliRunner()
    with runner.isolated_filesystem():
        # create mock file
        Path("sample.xls").touch()
        result = runner.invoke(cli, ["sample.xls"])
        assert result.exit_code == 0, result.output
        convert_xls_to_xlsx.assert_called_once_with(Path("sample.xls"))
        Path("sample.xls").unlink()
