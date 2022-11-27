import click

from src.pets.clients.petsapiclient import PetApiClient
from src.pets.pets import pass_environment

petApiClient = PetApiClient('http://localhost:8080', 'https://gitlab.tiendanimal.com:8088/')


@click.command("describe-infra")
@pass_environment
def cli(ctx):
    click.echo('scopes...')
    click.echo('secrets...')
