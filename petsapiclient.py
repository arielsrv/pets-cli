import http
import json

import click
import requests
from requests import HTTPError

pets_api_url = "http://localhost:8080"
gitlab_url = "https://gitlab.tiendanimal.com:8088/"


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


def get_app_types():
    try:
        response = requests.get(pets_api_url + '/apps/types')
        response.raise_for_status()

        result = json.loads(response.text)

        return result

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')


def get_app(name):
    try:
        response = requests.get(pets_api_url + '/search/apps?app_name=' + name)
        response.raise_for_status()

        result = json.loads(response.text)

        return result

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')


def create_app(name, group_id, app_type_id):
    try:
        payload = dict(name=name, group_id=group_id, app_type_id=app_type_id)
        response = requests.post(pets_api_url + '/repositories', json=payload)
        response.raise_for_status()

        result = json.loads(response.text)

        return result

    except HTTPError as http_err:
        if http_err.response.status_code == http.HTTPStatus.CONFLICT:
            click.echo('')
            click.echo(click.style("project " + name + " already exist", fg='red'))
            raise SystemExit(0)

        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
