import subprocess

import click

from pets import pass_environment


@click.command("repo", short_help="Upgrade CLI.")
@pass_environment
def cli(ctx):
    """Upgrade pets-cli to the latest version."""
    subprocess.call(["curl -o- https://raw.githubusercontent.com/arielsrv/pets-cli/v0.0.6/install.sh | bash"],
                    shell=True)
