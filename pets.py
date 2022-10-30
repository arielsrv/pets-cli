#!/usr/bin/env python
import os
import subprocess

import click
import questionary

from clients import PetApiClient

petApiClient = PetApiClient('http://localhost:8080', 'https://gitlab.tiendanimal.com:8088/')


@click.group()
@click.version_option('0.0.3')
def cli():
    pass


class MultipleOptions(click.Option):
    def __init__(self, param_decls=None, **attrs):
        click.Option.__init__(self, param_decls, **attrs)
        if not isinstance(self.type, click.Choice):
            raise Exception('ChoiceOption type arg must be click.Choice')

    def prompt_for_value(self, ctx):
        val = questionary.select(self.prompt, choices=self.type.choices).unsafe_ask()
        return val


@click.command()
@click.argument('name')
def get(name):
    click.echo('Getting ... ' + name)
    result = petApiClient.get_app(name)
    subprocess.call("git clone " + result['url'] + " " + name, shell=True)
    with open(name + '/.pets', 'w') as f:
        f.write('application_name: ' + name)


@click.command()
def groups():
    click.echo(click.style('Listing groups ...', fg='cyan'))
    result = petApiClient.get_groups()
    for group in result:
        print(group['name'])


@click.command()
@click.option('-n', '--name', required=True, prompt=True)
@click.option('-g', '--group', required=True, prompt=True,
              type=click.Choice(list(map(lambda x: x['name'], petApiClient.get_groups())), case_sensitive=False),
              cls=MultipleOptions)
@click.option('-t', '--app_type', required=True, prompt=True,
              type=click.Choice(list(map(lambda x: x['name'], petApiClient.get_app_types())), case_sensitive=False),
              cls=MultipleOptions)
def create_app(name, group, app_type):
    click.echo('Creating app ... ')
    click.echo('\tName: ' + name)
    click.echo('\tGroup: ' + group)
    click.echo('\tApplication Type: ' + app_type)

    group_response = next((x for x in petApiClient.get_groups() if x['name'] == group), None)
    app_type_response = next((x for x in petApiClient.get_app_types() if x['name'] == app_type), None)
    create_project_response = petApiClient.create_app(name, group_response['id'], app_type_response['id'])

    click.echo(click.style('\tRepo Url: ' + create_project_response['url'], fg='cyan'))

    click.echo('')
    click.echo('To download app use ' + click.style('pets get ' + name, fg='cyan'))


@click.command()
def get_token():
    click.echo(os.environ.get('GITLAB_TOKEN'))


@click.command()
def upgrade():
    subprocess.call(["curl -o- https://raw.githubusercontent.com/arielsrv/pets-cli/v0.0.3/install.sh | bash"],
                    shell=True)


cli.add_command(groups)
cli.add_command(create_app)
cli.add_command(get)
cli.add_command(get_token)
cli.add_command(upgrade)

if __name__ == '__main__':
    cli()
