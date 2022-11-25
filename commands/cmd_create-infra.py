import click

from clients import PetApiClient
from common.pets_file import get_app_name
from pets import pass_environment

petApiClient = PetApiClient('http://localhost:8080', 'https://gitlab.tiendanimal.com:8088/')


@click.group("create-infra")
@pass_environment
def cli(ctx):
    click.echo('create-infra')


@click.command()
@click.option('-n', '--name')
@pass_environment
def scope(ctx, name):
    appname = get_app_name()
    click.echo(click.style('creando scope ' + name + '... ', fg='cyan'))
    click.echo(click.style('url: https://{name}.{appname}.iskaypet.io'.format(name=name, appname=appname), fg='cyan'))


@click.command()
@click.option('-n', '--name')
@click.option('-v', '--value')
@pass_environment
def secret():
    click.echo('Secret created.')


cli.add_command(scope)
cli.add_command(secret)
