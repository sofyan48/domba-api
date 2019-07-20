from app import etcd_client as client
from etcd import EtcdKeyNotFound
from etcd import EtcdException
import ast


def create_dirs(stored):
    try:
        client.write("/"+stored, None, dir=True)
    except EtcdException as e:
        print(e)
        return None
    else:
        return True

def insert_data(stored, key, data):
    try:
        data = client.write("/"+stored+"/"+key, data)
    except EtcdException as e:
        raise e
    else:
        return data.key

def delete(stored, key):
    try:
        b = client.delete("/"+stored+"/"+key, recursive=True, dir=True)
    except EtcdException as e:
        raise e
    else:
        return b.key

def read_by_id(stored, key):
    try:
        a = client.read("/"+stored+"/"+key)
    except EtcdKeyNotFound as e:
        raise e
    else:
        return a.value

def read_all(stored):
    result = list()
    try:
        a = client.read("/"+stored)
    except EtcdKeyNotFound as e:
        raise e
    else:
        for child in a.children:
            data = ast.literal_eval(child.value)
            result.append(data)
    return result


def read_all_key(stored):
    result = list()
    try:
        a = client.read("/"+stored)
    except EtcdKeyNotFound as e:
        raise e
    else:
        for child in a.children:
            data = ast.literal_eval(child.value)
            result.append(int(data['key']))
    return result

def update(stored, key, data):
    try:
        delete(stored, str(key))
    except Exception as e:
        raise e
    try:
        data = insert_data(stored, key, data)
    except Exception as e:
        raise e
    else:
        return data
        
