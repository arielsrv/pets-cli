import os

import click

from pets.main import pass_environment


@click.command("get-token")
@pass_environment
def cli(ctx):
    click.echo(os.environ.get('GITLAB_TOKEN'))
