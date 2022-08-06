from . import BASE_URL
import requests

def messages(token):

    url = BASE_URL + '/messages'
    params = {
            'page': 1,
        }
    headers = {
            'Authorization': f'Bearer {token}',
            'accept': 'application/ld+json',
        }
    response = requests.get(
            url=url,
            params=params,
            headers=headers
        ).json()
    return response
