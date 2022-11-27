import click


def get_app_name(petsFileName):
    try:
        with open(petsFileName) as f:
            appname = f.readline().split(':')[1].strip()
            return appname

    except FileNotFoundError:
        click.echo('Para usar esta función es necesario estar en la carpeta de la aplicación. ')
    except Exception:
        click.echo('Error interno. Vuelve a descargar la aplicación con el commando get. ')
