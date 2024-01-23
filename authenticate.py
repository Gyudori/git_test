import requests
from getpass import getpass
import urllib
from pathlib import Path
import json


def get_url(server, region):
    if server == "dev":
        server_part = "dev."
    elif server == "stage":
        server_part = "stage."
    elif server == "qa":
        server_part = "qa."
    elif server == "prod" or server == "production":
        server_part = ""
    else:
        raise Exception("invalid server type found.")

    if region == "us":
        return "api." + server_part + "cupix.works"
    elif region == "eu":
        return "api." + server_part + "cupix-eu.works"
    elif region == "au":
        return "api." + server_part + "cupix-au.works"

    raise Exception("unsupportedRegion")


def get_api_url(server="prod", region="us"):
    return "https://{url}/api/v1".format(url=get_url(server, region))


def build_url(base_url, *res, **params):
    url = f'{base_url}/{"/".join(map(str, res))}'
    if params:
        url = "{}?{}".format(url, urllib.parse.urlencode(params))
    return url

def get_refresh_token(api_url):
    cache_filepath = Path().cwd().joinpath('cupix-auth.json')
    if cache_filepath.exists():
        with open(cache_filepath, 'r') as file:
            cache = json.load(file)
            refresh_token = cache['refresh_token']

    else:
        url = build_url(api_url, "authenticate")


        email = input("User email: ")
        password = getpass("Password: ")

        request = {
            "grant_type": "email",
            "team_domain": "cupix",
            "email": email,
            "password": password,
        }

        res = requests.post(build_url(api_url, "authenticate"), json=request)
        print(res.json())

        refresh_token = res.json()["result"]["refresh_token"]

        cupix_auth = {}
        cupix_auth['refresh_token'] = refresh_token
        with open(cache_filepath, 'w') as file:
            json.dump(cupix_auth, file)
    
    return refresh_token


def get_access_token(api_url):
    refresh_token = get_refresh_token(api_url)

    request = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
    }

    res = requests.post(build_url(api_url, "authenticate"), json=request)

    return res.json()["result"]["access_token"]


def main():
    api_url = get_api_url()

    access_token = get_access_token(api_url)

    headers = {
        'X-CUPIX-AUTH': access_token,
        'X-CUPIX-TEAM-DOMAIN': 'cupix'
    }
    session = requests.Session()
    session.headers.update(headers)

    

    res = session.get(
        build_url(
            api_url,
            "clusters",
            capture_id=315745,
            fields="id,name,kind,capture,parent,meta,skat_result_type",
        )
    )
    print(res.json())


if '__main__' == __name__:
    main()









