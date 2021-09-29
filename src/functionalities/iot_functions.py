from os import system as execute
from posixpath import expanduser
import requests

from src.functionalities.read_credentials import *

FLASK_SERVER_URL = read_credentials('flask')['URL']

# PS4 related

# IDEIA: iniciar jogos específicos por meio da Liza

def start_ps4():
    execute('ps4-waker')

def standby_ps4():
    execute('ps4-waker standby')

def start_chiaki():
    execute('Chiaki')


# Flask server

def check_flask_server():

    try:
        if ((requests.get(FLASK_SERVER_URL + '/isalive')).status_code == 200):
            return True
    except:
        return False

def stop_flask_server():
    try:
        requests.get(FLASK_SERVER_URL + '/shutdown')
    except:
        print('servidor parado')

def start_flask_server():
    execute('nohup ${HOME}/Server/start_server.sh &')

# Others

def start_discord():
    execute('discord')
    