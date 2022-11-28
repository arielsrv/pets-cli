import random
import re
import time

import click

from src.pets.common.pets_file import get_app_name
from src.pets.consts.consts import PETS_FILE_NAME
from src.pets.pets import pass_environment


def validate_version(ctx, param, value):
    pattern = re.compile(
        r'^([0-9]+)\.([0-9]+)\.([0-9]+)(?:-([0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?(?:\+[0-9A-Za-z-]+)?$')
    if not re.fullmatch(pattern, value[0]):
        raise click.BadParameter("Formato de versión inválido. Ej: 0.0.1-hello-world")

    return value[0]


@click.command("create-version")
@click.argument('version', nargs=-1, callback=validate_version, type=click.STRING)
@pass_environment
def cli(ctx, version):
    appname = get_app_name(PETS_FILE_NAME)

    items = range(2000)

    def process_slowly():
        time.sleep(0.002 * random.random())

    with click.progressbar(
            items, label="Creando versión " + version, fill_char=click.style("#", fg="green")
    ) as bar:
        for _ in bar:
            process_slowly()
