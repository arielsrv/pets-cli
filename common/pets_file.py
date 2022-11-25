import click


def get_app_name():
    try:
        with open('.pets') as f:
            appname = f.readline().split(':')[1].strip()
            return appname

    except FileNotFoundError:
        click.echo('Para crear versiones es necesario estar en el directorio de la aplicación. ')
    except Exception:
        click.echo('Error interno. Vuelve a descargar la aplicación con el commando get. ')