import click

from pets.pets import pass_environment


@click.command("version")
@pass_environment
def cli(ctx):
    click.echo('0.0.8')
