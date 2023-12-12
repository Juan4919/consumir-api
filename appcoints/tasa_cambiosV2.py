import requests 
from config import APIKEY

#consulta todas las monedas
url=f"https://rest.coinapi.io/v1/assets/?apikey={APIKEY}"
r = requests.get(url)
if r.status_code != 200:
    raise Exception("Error en consulta codigo:{}".format(r.status_code))


lista_general= r.json()
lista_criptos=[]

for dic in lista_general:   
    if dic["type_is_crypto"] == 1:
        lista.criptos.append(dic["asset_id"])
        
print("Total:",len(lista_general))
print("Criptos:",len(lista_criptos))
print("No criptos:",len(lista_general)-len(lista_criptos))
print("lista:",lista_criptos)