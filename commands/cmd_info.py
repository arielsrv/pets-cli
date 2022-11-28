import click

from clients.petsapi import PetApiClient
from consts.urls import PETS_API_URL, GITLAB_API_URL
from pets import pass_environment

petApiClient = PetApiClient(PETS_API_URL, GITLAB_API_URL)


@click.command("info")
@pass_environment
def cli(ctx):
    try:
        with open('.pets') as f:
            appname = f.readline().split(':')[1].strip()

            appresponse = petApiClient.get_app(appname)
            click.echo(appresponse.url)

    except FileNotFoundError:
        click.echo('Para crear versiones es necesario estar en el directorio de la aplicación. ')
    except Exception:
        click.echo('Error interno. Vuelve a descargar la aplicación con el commando get. ')
