import json
from os import path, getcwd

def read_credentials(key):
    with open(path.abspath(getcwd())+'/src/functionalities/credentials.json') as credentials:
        d = json.load(credentials)
        return d[f'{key}']