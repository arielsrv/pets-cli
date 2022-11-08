import sys

import click
import questionary

from clients import PetApiClient
from pets import pass_environment

petApiClient = PetApiClient('http://localhost:8080', 'https://gitlab.tiendanimal.com:8088/')


@click.command("create-app")
@click.option('-n', '--name')
@click.option('-g', '--group')
@click.option('-t', '--app_type')
@pass_environment
def cli(ctx, name, group, app_type):
    if not name:
        name = questionary.text("App name ").ask()

    if not name:
        sys.exit()

    if not group:
        groups_names = list(map(lambda x: x.name, petApiClient.get_groups()))
        group = questionary.autocomplete(
            'Choose a group',
            choices=groups_names,
            match_middle=True,
            style=None,
        ).ask()

    if not group:
        sys.exit()

    if not app_type:
        apps_types_names = list(map(lambda x: x.name, petApiClient.get_app_types()))
        app_type = questionary.autocomplete(
            'Choose a app type ',
            choices=apps_types_names,
            match_middle=True,
            style=None,
        ).ask()

    if not app_type:
        sys.exit()

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
