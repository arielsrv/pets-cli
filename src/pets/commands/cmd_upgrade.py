import subprocess

import click

from src.pets.pets import pass_environment


@click.command("upgrade")
@pass_environment
def cli(ctx):
    subprocess.call(["curl -o- https://raw.githubusercontent.com/arielsrv/pets-cli/v0.0.8/install.sh | bash"],
                    shell=True)
