import click

from src.pets.clients.petsapiclient import PetApiClient
from src.pets.common.pets_file import get_app_name
from src.pets.pets import pass_environment, PETS_FILE_NAME

petApiClient = PetApiClient('http://localhost:8080', 'https://gitlab.tiendanimal.com:8088/')


@click.group("create-infra")
@pass_environment
def cli(ctx):
    click.echo('create-infra')


@click.command()
@click.option('-n', '--name')
@pass_environment
def scope(ctx, name):
    appname = get_app_name(PETS_FILE_NAME)
    click.echo(click.style('creando scope ' + name + '... ', fg='cyan'))
    click.echo()
    click.echo(
        click.style('Host: https://{name}.{appname}.iskaypetapps.io'.format(name=name, appname=appname), fg='yellow'))
    click.echo(click.style(
        'NewRelic: https://newrelic.com?scope={name}&app_name={appname}'.format(name=name, appname=appname),
        fg='cyan'))
    click.echo(click.style(
        'Logs: https://kibana.com?scope={name}&app_name={appname}'.format(name=name, appname=appname),
        fg='cyan'))
    click.echo(click.style(
        'Metrics: https://datadog.com?scope={name}&app_name={appname}'.format(name=name, appname=appname),
        fg='cyan'))
    click.echo()


@click.command()
@click.option('-n', '--name')
@click.option('-v', '--value')
@pass_environment
def secret(ctx, name, value):
    click.echo(name)
    click.echo(value)
    click.echo('Secret created.')


cli.add_command(scope)
cli.add_command(secret)
