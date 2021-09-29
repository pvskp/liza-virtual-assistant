from os import system as execute
import requests
import json

from read_credentials import *

FLASK_SERVER_URL = read_credentials('flask')['URL']

# PS4 related

def start_ps4():
    execute('ps4-waker')

def standby_ps4():
    execute('ps4-waker standby')

def start_chiaki():
    execute('Chiaki')


# Flask server

def check_flask_server():
    if ((requests.get(FLASK_SERVER_URL + '/isalive')).status_code == 200):
        return True
    
    return False

def stop_flask_server():
    requests.get(FLASK_SERVER_URL + '/shutdown')

def start_flask_server():
    execute('${HOME}/Server/start_server.sh')

# Others

def start_discord():
    execute('discord')
    