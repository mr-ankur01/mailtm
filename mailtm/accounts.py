
import requests,json

def create(address: str, password: str):
    url = 'https://api.mail.tm/accounts'
    body = {
        'address': address,
        'password': password
    }
    headers = {
        'accept': 'application/ld+json',
        'Content-Type': 'application/ld+json',
    }
    response = requests.post(
        url=url, 
        data=json.dumps(body), 
        headers=headers
    )
    req = response.json()
    return req
