#!/usr/bin/env python
import os
import subprocess

import click

from clients import PetApiClient
from common import MultipleOptions

petApiClient = PetApiClient('http://localhost:8080', 'https://gitlab.tiendanimal.com:8088/')


@click.group()
@click.version_option('0.0.5')
def cli():
    pass


@click.command()
@click.argument('name')
def get(name):
    """Get IskayPet app"""
    click.echo('Getting ... ' + name)
    appresponse = petApiClient.get_app(name)
    subprocess.call("git clone " + appresponse.url + " " + name, shell=True)
    with open(name + '/.pets', 'w') as stream:
        stream.write('application_name: ' + name)


@click.command()
def groups():
    """List available groups."""
    click.echo(click.style('Listing groups ...', fg='cyan'))
    result = petApiClient.get_groups()
    for group in result:
        print(group.name)


@click.command()
@click.option('-n', '--name', required=True, prompt=True)
@click.option('-g', '--group', required=True, prompt=True,
              type=click.Choice(list(map(lambda group: group.name, petApiClient.get_groups())), case_sensitive=False),
              cls=MultipleOptions)
@click.option('-t', '--app_type', required=True, prompt=True,
              type=click.Choice(list(map(lambda apptype: apptype.name, petApiClient.get_app_types())),
                                case_sensitive=False),
              cls=MultipleOptions)
def create_app(name, group, app_type):
    """Creates IskayPet app."""
    click.echo('Creating app ... ')
    click.echo('\tName: ' + name)
    click.echo('\tGroup: ' + group)
    click.echo('\tApplication Type: ' + app_type)

    group_response = next((x for x in petApiClient.get_groups() if x.name == group), None)
    app_type_response = next((x for x in petApiClient.get_app_types() if x.name == app_type), None)
    create_project_response = petApiClient.create_app(name, group_response.id, app_type_response.id)

    click.echo(click.style('\tRepo Url: ' + create_project_response['url'], fg='cyan'))

    click.echo('')
    click.echo('To download app use ' + click.style('pets get ' + name, fg='cyan'))


@click.command()
def get_token():
    """Get IskayPet token."""
    click.echo(os.environ.get('GITLAB_TOKEN'))


@click.command()
def upgrade():
    """Upgrade pets-cli to the latest version."""
    subprocess.call(["curl -o- https://raw.githubusercontent.com/arielsrv/pets-cli/v0.0.5/install.sh | bash"],
                    shell=True)


@click.command()
def create_version():
    click.echo('')


cli.add_command(groups)
cli.add_command(create_app)
cli.add_command(get)
cli.add_command(get_token)
cli.add_command(upgrade)
cli.add_command(create_version)

if __name__ == '__main__':
    result = petApiClient.get_app_types()
    for type in list(map(lambda x: x.name, result)):
        print(type)
    cli()
