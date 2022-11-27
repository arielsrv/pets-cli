import unittest

from click.testing import CliRunner

from src.pets.commands.cmd_version import cli


class CmdVersionTest(unittest.TestCase):
    def test_get_version(self):
        runner = CliRunner()
        actual = runner.invoke(cli)
        self.assertEqual(0, actual.exit_code)
        self.assertEqual('0.0.8\n', actual.output)


if __name__ == '__main__':
    unittest.main()
