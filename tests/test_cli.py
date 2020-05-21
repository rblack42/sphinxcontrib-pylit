from click.testing import CliRunner
from sphinxcontrib.pylit.cli import cli

def test_cli():
    runner = CliRunner()
    result = runner.invoke(cli, ['Roie'])
    assert result.exit_code == 0
    assert 'Roie' in result.output
