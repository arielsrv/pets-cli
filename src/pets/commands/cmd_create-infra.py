import click

import src
from src.pets.clients.petsapiclient import PetApiClient
from src.pets.common.pets_file import get_app_name
from src.pets.consts.consts import PETS_API_URL, GITLAB_API_URL, PETS_FILE_NAME
from src.pets.pets import pass_environment

petApiClient = PetApiClient(PETS_API_URL, GITLAB_API_URL)


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
    appName = get_app_name(PETS_FILE_NAME)
    appresponse = petApiClient.get_app(appName)

    secretresponse = petApiClient.create_secret(appresponse.id, name, value)

    apiUrl = "{baseUrl}{snippetUrl}".format(baseUrl=src.pets.pets.PETS_API_URL, snippetUrl=secretresponse.snippet_url)
    click.echo('Secret created: {apiUrl}'.format(apiUrl=apiUrl))


cli.add_command(scope)
cli.add_command(secret)
