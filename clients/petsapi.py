import http
import json

import click
import requests
from requests import HTTPError

from clients.responses.appresponse import AppResponse
from clients.responses.apptyperesponse import AppTypeResponse
from clients.responses.groupresponse import GroupResponse
from clients.responses.secretresponse import SecretResponse
from common.jsonextensions import from_list


class PetApiClient:

    def __init__(self, petsapiurl, gitlaburl):
        self.petsapiurl = petsapiurl
        self.gitlaburl = gitlaburl

    def get_groups(self):
        try:
            response = requests.get(self.petsapiurl + '/apps/groups')
            response.raise_for_status()

            return from_list(GroupResponse.from_dict, json.loads(response.text))

        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')

    def get_app_types(self):
        try:
            response = requests.get(self.petsapiurl + '/apps/types')
            response.raise_for_status()

            return from_list(AppTypeResponse.from_dict, json.loads(response.text))

        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')

    def get_app(self, name):
        try:
            response = requests.get(self.petsapiurl + '/apps/search?app_name=' + name)
            response.raise_for_status()

            result = AppResponse.from_dict(json.loads(response.text))

            return result

        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')

    def create_app(self, name, group_id, app_type_id):
        try:
            payload = dict(name=name, group_id=group_id, app_type_id=app_type_id)
            response = requests.post(self.petsapiurl + '/apps', json=payload)
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

    def create_secret(self, appId, key, value):
        try:
            payload = dict(key=key, value=value)
            apiUrl = "{baseUrl}/apps/{appId}/secrets".format(baseUrl=self.petsapiurl, appId=appId)
            response = requests.post(apiUrl, json=payload)
            response.raise_for_status()

            return SecretResponse.from_dict(json.loads(response.text))

        except HTTPError as http_err:
            if http_err.response.status_code == http.HTTPStatus.CONFLICT:
                click.echo('')
                click.echo(click.style("secret " + key + " already exist", fg='red'))
                raise SystemExit(0)

            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
