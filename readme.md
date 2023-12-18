# Aplicación de consulta de valor actual de criptomonedas

Programa hecho en python para recuperar el valor en euros de una criptomoneda
desde www.coinapi.io

## Instalación
-Obtener una apikey en https://docs.coinapi.io/ ingrese un    correo valido y dar click al boton GET A FREE APIKEY

-Renombrar el fichero config_template.py a config.py

-Agregar dentro de config.py el api key de esta manera:

```
APIKEY = "AQUI VA SU APIKEY"
```

## Instalación de dependencias(librerias)
-Crear un entorno virtual de python con una de estas opciones
```
py -m venv entorno
python -m venv entorno
python3 -m venv entorno
```

-Activar el entorno e instalar los requerimientos 
```
windows - .\entorno\Scripts\activate
mac o linux - source entorno/bin/activate 

pip install -r requirements.txt
```

- Utiliza las librerias de pytest y requests
