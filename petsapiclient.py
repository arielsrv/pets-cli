import json

import requests
from requests import HTTPError

pets_api_url = "http://localhost:8080"


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
