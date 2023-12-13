import requests
from config import APIKEY

moneda_cripto = input("Ingrese una criptomoneda conocida: ").upper()

while moneda_cripto != "" and moneda_cripto.isalpha():
    #invocando al metodo get con la url especifica
    url = f"https://rest.coinapi.io/v1/exchangerate/{moneda_cripto}/EUR?apikey={APIKEY}"
    r = requests.get(url)

    #ejercicio 1 como capturamos el rate
    respuesta = r.json()#obtener la respuesta en formato diccionario

    #ejercicio 2, como capturo errores de peticion http

    if r.status_code == 200:
        #print("rate: ",respuesta['rate'] )#2084.6980485137988 cambie a 2084.69€
        print( "{:.2f}€".format( respuesta['rate'] ) )#2084.69€
        break
    else:
        print("error:",respuesta['error'])

    moneda_cripto = input("Ingrese una criptomoneda conocida: ").upper()  