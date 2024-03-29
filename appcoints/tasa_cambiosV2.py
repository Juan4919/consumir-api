import requests
from config import APIKEY

#consulta de todas las monedas
url=f"https://rest.coinapi.io/v1/assets/?apikey={APIKEY}"
r = requests.get(url)
if r.status_code != 200:
   raise Exception("Error en consulta codigo:{}".format(r.status_code)) 

lista_general= r.json()
lista_criptos=[]

for dic in lista_general:
    if dic["type_is_crypto"] == 1:
        lista_criptos.append(dic["asset_id"] )#["EXFC","SPACEID"]

print("Total:",len(lista_general))
print("Criptos:",len(lista_criptos))
print("No criptos:",len(lista_general)-len(lista_criptos))
#print("Lista:",lista_criptos)

########################################################################

moneda_cripto = input("Ingrese una criptomoneda conocida: ").upper()

while moneda_cripto != "" and moneda_cripto.isalpha():
    if moneda_cripto in lista_criptos:
        url = f"https://rest.coinapi.io/v1/exchangerate/{moneda_cripto}/EUR?apikey={APIKEY}"
        r = requests.get(url)
        respuesta = r.json()
        if r.status_code == 200:
            print( "{:.2f}€".format( respuesta['rate'] ) )#2084.69€
            break
        else:
            print("error:",respuesta['error'])

    moneda_cripto = input("Ingrese una criptomoneda conocida: ").upper() 