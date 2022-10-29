#!/usr/bin/env python
import json
import os
import string

import click
import questionary
import requests as requests
from requests import HTTPError

pets_api_url = "http://localhost:8080"


@click.group()
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


@click.command()
def groups():
    click.echo(click.style('Listing groups ...', fg='cyan'))
    result = get_groups()
    for group in result:
        print(group['name'])


def get_groups():
    try:
        response = requests.get(pets_api_url + '/repositories/groups')
        response.raise_for_status()

        result = json.loads(response.text)

        return result

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')


@click.command()
@click.option('-n', '--name', required=True, prompt=True)
@click.option('-g', '--group', required=True, prompt=True,
              type=click.Choice(list(map(lambda x: x['name'], get_groups())), case_sensitive=False),
              cls=MultipleOptions)
@click.option('-t', '--app_type', required=True, prompt=True,
              type=click.Choice(['backend', 'frontend'], case_sensitive=False), cls=MultipleOptions)
def create_app(name, group, app_type):
    click.echo('Creating ' + name + ", please wait ...")
    click.echo('\tGroup: ' + group)
    click.echo('\tApplication Type: ' + app_type)
    click.echo(click.style('Done', fg='green'))

    click.echo('')
    click.echo('To download app use ' + click.style('pets get ' + name, fg='cyan'))


@click.command()
@click.argument('hash-type')
def describe_infra(hash_type):
    click.echo('App infra ... ' + hash_type)


@click.command()
def upgrade():
    click.echo('App infra ... ')


@click.command()
def get_token():
    click.echo(gitlab_token)


def register_commands():
    cli.add_command(groups)
    cli.add_command(create_app)
    cli.add_command(get)
    cli.add_command(describe_infra)
    # cli.add_command(upgrade)
    cli.add_command(get_token)


register_commands()
gitlab_token = os.environ.get('GITLAB_TOKEN')
if __name__ == '__main__':
    if gitlab_token is not None:
        cli()
    else:
        click.echo(click.style('GITLAB_TOKEN variable is missing', fg='red'), err=True)
