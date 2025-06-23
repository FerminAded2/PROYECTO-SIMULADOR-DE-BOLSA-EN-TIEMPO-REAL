import requests
import random
import datetime

def obtener_datos(api_key, simbolo):
    """
    Devuelve los datos reales de Alpha Vantage si están disponibles.
    Si no, devuelve un diccionario con datos simulados.
    """
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={simbolo}&apikey={api_key}"
    try:
        respuesta = requests.get(url, timeout=10)
        datos = respuesta.json()

        if "Time Series (Daily)" in datos:
            return datos

        raise ValueError("La API no devolvió datos válidos.")

    except Exception:
        # Datos simulados con precio ficticio
        precio_simulado = round(random.uniform(100, 300), 2)
        fecha_actual = datetime.datetime.today().strftime('%Y-%m-%d')
        datos_simulados = {
            "Time Series (Daily)": {
                fecha_actual: {
                    "4. close": str(precio_simulado)
                }
            }
        }
        return datos_simulados
