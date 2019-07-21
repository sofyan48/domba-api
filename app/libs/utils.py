from app.models import model
import requests
import json
import datetime


def get_http(url, param=None, header=None):
    json_data = None
    if param:
        json_data = param
    get_func = requests.get(url, params=json_data, headers=header)
    data = get_func.json()
    return data


def get_datetime():
    now = datetime.datetime.now()
    return str(now)

def check_unique(stored, field, value, key=None):
    all_data = model.read_all(stored)
    results = False
    for i in all_data:
        if i[field] == value:
            if key is not None:
                if key == i['key']:
                    results = False
                else:
                    results = True
            else:
                results = True
            break
    return results

def get_last_key(stored):
    try:
        all_data = model.read_all_key(stored)
    except Exception:
        return str(1)
    else:
        key = max(all_data)
        return str(key+1)