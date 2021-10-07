import json
from os import getcwd

def read_credentials(key):
    with open(getcwd()+'/src/functionalities/credentials.json') as credentials:
        return (json.load(credentials))[f'{key}']
