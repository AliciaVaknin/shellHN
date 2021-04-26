from click.testing import CliRunner
from shell_hn import top


def test_top():
    runner = CliRunner()
    result = runner.invoke(top)
    assert 'The top stories in Hacker News:' in result.output
    assert result.exit_code == 0

