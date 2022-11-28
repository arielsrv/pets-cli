import click

from src.pets.clients.petsapiclient import PetApiClient
from src.pets.consts.consts import PETS_API_URL, GITLAB_API_URL
from src.pets.pets import pass_environment

petApiClient = PetApiClient(PETS_API_URL, GITLAB_API_URL)


@click.command("groups")
@pass_environment
def cli(ctx):
    result = petApiClient.get_groups()
    for group in result:
        print(group.name)
