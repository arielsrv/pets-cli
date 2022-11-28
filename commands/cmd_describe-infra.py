import click

from clients.petsapi import PetApiClient
from consts.urls import PETS_API_URL, GITLAB_API_URL
from pets import pass_environment

petApiClient = PetApiClient(PETS_API_URL, GITLAB_API_URL)


@click.command("describe-infra")
@pass_environment
def cli(ctx):
    click.echo('scopes...')
    click.echo('secrets...')
