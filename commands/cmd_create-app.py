import sys

import click
import questionary

from pets import pass_environment
from clients.petsapi import PetApiClient
from pets import GITLAB_API_URL, PETS_API_URL


petApiClient = PetApiClient(PETS_API_URL, GITLAB_API_URL)
from questionary import Style

custom_style_fancy = Style(
    [
        ("answer", "fg:#8fce00 bg:#000000 bold"),
    ]
)


@click.command("create-app")
@click.option('-n', '--name')
@click.option('-g', '--group')
@click.option('-t', '--type')
@pass_environment
def cli(ctx, name, group, type):
    if not name:
        name = questionary.text('App name', style=custom_style_fancy).ask()

    if not name:
        sys.exit()

    if not group:
        groups_names = list(map(lambda x: x.name, petApiClient.get_groups()))
        group = questionary.autocomplete(
            'Choose a group',
            choices=groups_names,
            match_middle=True,
            style=custom_style_fancy
        ).ask()

    if not group:
        sys.exit()

    if not type:
        apps_types_names = list(map(lambda x: x.name, petApiClient.get_app_types()))
        type = questionary.autocomplete(
            'Choose a app type',
            choices=apps_types_names,
            match_middle=True,
            style=custom_style_fancy,
        ).ask()

    if not type:
        sys.exit()

    click.echo('Creating app ... ')
    click.echo('\tName: ' + name)
    click.echo('\tGroup: ' + group)
    click.echo('\tApplication Type: ' + type)

    group_response = next((x for x in petApiClient.get_groups() if x.name == group), None)
    app_type_response = next((x for x in petApiClient.get_app_types() if x.name == type), None)
    create_project_response = petApiClient.create_app(name, group_response.id, app_type_response.id)

    click.echo(click.style('\tRepo Url: ' + create_project_response['url'], fg='cyan'))

    click.echo('')
    click.echo('To download app use ' + click.style('pets get ' + name, fg='cyan'))
