from subprocess import call

import click

from src.pets.clients.petsapiclient import PetApiClient
from src.pets.pets import pass_environment, PETS_API_URL, GITLAB_API_URL

petApiClient = PetApiClient(PETS_API_URL, GITLAB_API_URL)


@click.command("get")
@click.argument('name')
@pass_environment
def cli(ctx, name):
    click.echo('Getting ... ' + name)
    appresponse = petApiClient.get_app(name)
    call("git clone " + appresponse.url + " " + name, shell=True)
    with open(name + '/.pets', 'w') as stream:
        stream.write('application_name: ' + name)
