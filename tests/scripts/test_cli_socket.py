import unittest

from click.testing import CliRunner

from scripts import cli_socket

class TestRun(unittest.TestCase):

    def test_pr4e_exists(self):
        # Connect to google and ensure it exists (if should once I have an internet connection)
        runner = CliRunner()
        result = runner.invoke(
            cli_socket.cli, 
            [
                'data.pr4e.org',
                'http://data.pr4e.org/page1.htm',
                # '80'
                ], 
            )
        assert result.exit_code == 0, "Wrong exit code: {}".format(result.exit_code)
        assert '<h1>' in result.output, result.output
        assert '<p>' in result.output, result.output

        cli_socket.cli()