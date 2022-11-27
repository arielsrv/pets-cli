import click

from src.pets.clients.petsapiclient import PetApiClient

petApiClient = PetApiClient('http://localhost:8080', 'https://gitlab.tiendanimal.com:8088/')


@click.command("deploy")
@click.option('-s', '--scope')
@click.option('-v', '--version')
@click.option('-str', '--strategy', type=click.Choice(['BLUE-GREEN', 'CANARY', 'ALL-IN'], case_sensitive=False))
def cli(scope, version, strategy):
    click.echo('scopes...')
    click.echo('secrets...')
