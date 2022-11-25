import click

from clients import PetApiClient
from common.pets_file import get_app_name
from pets import pass_environment

petApiClient = PetApiClient('http://localhost:8080', 'https://gitlab.tiendanimal.com:8088/')


@click.command("describe-infra")
@pass_environment
def cli(ctx):
    click.echo('scopes...')
    click.echo('secrets...')