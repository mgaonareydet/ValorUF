import requests
import json
import pyperclip as clip
import datetime
import sys

current_date = datetime.date.today()
first_day_of_current_month = current_date.replace(day=1)
last_day_of_previous_month = first_day_of_current_month - datetime.timedelta(days=1)
FECHA_DEFAULT = last_day_of_previous_month.strftime('%d-%m-%Y')


try:
    FECHAPERIODO = sys.argv[1]
    if len(FECHAPERIODO) != 6:
        clip.copy('Periodo mal ingresado')
    else:
        FECHA = datetime.date(int(FECHAPERIODO[:4]),int(FECHAPERIODO[5:6])+1,1) - datetime.timedelta(days=1)
        FECHA = FECHA.strftime('%d-%m-%Y')
except:
    FECHA = FECHA_DEFAULT


URL = 'https://mindicador.cl/api/uf/'

URL_CONSULTA = URL+FECHA

response = requests.get(URL_CONSULTA, verify=False)

responseJSON = json.loads(response.text)

valor_uf = responseJSON['serie'][0]['valor']
valor_uf = str(valor_uf)
valor_uf = valor_uf.replace('.',',')
clip.copy(valor_uf)