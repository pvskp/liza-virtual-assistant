import requests
import json

def get_currency():
    dollar_currency = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
    dollar_currency = dollar_currency.json()
    value_in_reais = dollar_currency['USDBRL']['bid']
    reais = int((float(value_in_reais) // 1))
    centavos = (int((float(value_in_reais) % 1)*100))
    return reais, centavos