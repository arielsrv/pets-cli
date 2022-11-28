import click

from src.pets.clients.petsapiclient import PetApiClient
from src.pets.pets import pass_environment, PETS_API_URL, GITLAB_API_URL

petApiClient = PetApiClient(PETS_API_URL, GITLAB_API_URL)


@click.command("describe-infra")
@pass_environment
def cli(ctx):
    click.echo('scopes...')
    click.echo('secrets...')
