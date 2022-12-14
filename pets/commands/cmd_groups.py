import click

from pets.clients.petsapi import PetApiClient
from pets.consts.urls import PETS_API_URL, GITLAB_API_URL
from pets.main import pass_environment

petApiClient = PetApiClient(PETS_API_URL, GITLAB_API_URL)


@click.command("groups")
@pass_environment
def cli(ctx):
    result = petApiClient.get_groups()
    for group in result:
        print(group.name)
