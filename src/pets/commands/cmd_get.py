import subprocess

import click

from src.pets.clients.petsapiclient import PetApiClient
from src.pets.pets import pass_environment

petApiClient = PetApiClient('http://localhost:8080', 'https://gitlab.tiendanimal.com:8088/')


@click.command("get")
@click.argument('name')
@pass_environment
def cli(ctx, name):
    click.echo('Getting ... ' + name)
    appresponse = petApiClient.get_app(name)
    subprocess.call("git clone " + appresponse.url + " " + name, shell=True)
    with open(name + '/.pets', 'w') as stream:
        stream.write('application_name: ' + name)