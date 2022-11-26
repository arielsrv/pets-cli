import subprocess

import click

from pets import pass_environment


@click.command("upgrade")
@pass_environment
def cli(ctx):
    subprocess.call(["curl -o- https://raw.githubusercontent.com/arielsrv/pets-cli/v0.0.6/install.sh | bash"],
                    shell=True)
