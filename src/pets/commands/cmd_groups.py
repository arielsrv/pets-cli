import click

from src.pets.clients.petsapiclient import PetApiClient
from src.pets.pets import pass_environment

petApiClient = PetApiClient('http://localhost:8080', 'https://gitlab.tiendanimal.com:8088/')


@click.command("groups")
@pass_environment
def cli(ctx):
    result = petApiClient.get_groups()
    for group in result:
        print(group.name)
