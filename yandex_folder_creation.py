import requests
from datetime import datetime


def get_headers(token_ya):
    return {
        'Content-Type': 'application/json',
        'Authorization': 'OAuth {}'.format(token_ya)
    }


def create_folder(token_ya):
    params = {
        "path": f"folder_{get_current_time()}"
    }
    creation = requests.put(url='https://cloud-api.yandex.net/v1/disk/resources', params=params, headers=get_headers(token_ya))
    return requests.get(url=f'https://cloud-api.yandex.net/v1/disk/resources/', params=params, headers=get_headers(token_ya))

def get_current_time():
    current_datetime = datetime.strftime(datetime.now(), "%d%H%M")
    return current_datetime



if __name__ == '__main__':
    print(create_folder(''))
