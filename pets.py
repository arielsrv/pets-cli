#!/usr/bin/env python

import click


@click.group()
def cli():
    pass


@click.command()
@click.argument('name')
@click.argument('group')
def create_app(name, group):
    click.echo('Creating ... ' + name)
    click.echo('Creating ... ' + group)


@click.command()
@click.argument('name')
def get(name):
    click.echo('Getting ... ' + name)


@click.command()
def groups():
    click.echo('List groups ... ')


@click.command()
def describe_infra():
    click.echo('App infra ... ')


@click.command()
def upgrade():
    click.echo('App infra ... ')


cli.add_command(groups)
cli.add_command(create_app)
cli.add_command(get)
cli.add_command(describe_infra)
cli.add_command(upgrade)

if __name__ == '__main__':
    cli()
