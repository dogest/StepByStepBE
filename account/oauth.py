import requests
from StepByStepBE.settings import client_id, client_secret


def get_access_token(code):
    url = f'https://github.com/login/oauth/access_token'
    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'code': code,
    }
    headers = {
        'Accept': 'application/json',
    }
    resp = requests.post(url, data=data, headers=headers)
    return resp.json().get('access_token')


def get_user_info(access_token):
    url = f'https://api.github.com/user'
    headers = {
        'Authorization': f'token {access_token}',
        'Accept': 'application/json',
    }
    resp = requests.get(url, headers=headers)
    return resp.json()
