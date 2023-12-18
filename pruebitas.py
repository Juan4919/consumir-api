respuesta={
"time": "2023-12-11T13:26:15.0000000Z",
"asset_id_base": "BTC",
"asset_id_quote": "EUR",
"rate": 39204.65040504416
}

#print(respuesta['rate'])
#print( respuesta.get('rate') )

errores= {
"error": "You didn't specify API key or it is incorrectly formatted. You should do it in: query string parameter `apikey`,  in http header named `X-CoinAPI-Key`,  in http header named `Authorization` or  as part of URL /apikey-YOUR-API-KEY/"
}

#print(errores["error"])

prueba= "MDMfdf"
#print(  prueba.upper() )

#print( prueba.isalpha() )#True 
"""
numero =2084.6980485137988
print(type(numero))
valor= "{:.2f}€".format(numero)
print(type(valor))
print( valor )
"""


lista=["EXFC","SPACEID"]

dato="EXFC"

for item in lista:
    if item==dato:
        print("se encuentra")

if dato in lista:
    print("SE ENCUENTRA")        
