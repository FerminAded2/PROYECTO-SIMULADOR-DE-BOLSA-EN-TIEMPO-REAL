import requests
import json

def obtener_datos(api_key, simbolo):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={simbolo}&apikey={api_key}"
    respuesta = requests.get(url)
    return respuesta.json()

def guardar_json(datos, nombre_archivo):
    with open(nombre_archivo, "w") as archivo:
        json.dump(datos, archivo, indent=4)

def mostrar_ultimo_cierre(datos):
    ultima_fecha = list(datos["Time Series (Daily)"].keys())[0]
    cierre = datos["Time Series (Daily)"][ultima_fecha]["4. close"]
    print(f"Última fecha: {ultima_fecha}")
    print(f"Precio de cierre: ${cierre}")

def documento ():

    """Para poder trabajar con una API, tuvimos que aprender conceptos nuevos.
    Obviamente una de las primeras preguntas que nos hicimos al pensar en este
    proyecto fue... "Como traemos la informacion que necesitamos ?"
    logicamante necesitamos una herramienta que nos ayude con esto ,a esto se le dice API
    que son las siglas de "Application Programming Interface" en criollo, el programa
    que se conecta/comunica con otra aplicacion/base de datos, y le dice... che maestro, traeme esto
    o aquello. Para que pase eso, necesitamos usar la libreria llamada request, la cual serviria para
    lo anteriormente mensionado. Entonces, podriamos pensar lo siquiente... Estamos en el laburo
    y queremos un cafe, para esto lo tenemos que pedir, pero la cafeteria que nos gusta no aparece en las apps de
    de pedidos, asi que no nos queda de otra que llamar,darle nuestra direccion y pedir. Bueno aca seria lo mismo,
    con request nosotros ponemos la direccion, en este caso el URL de donde tomaremos la informacion y siguiendo
    con la analogia anterior, el cafe con leche con medialuna seria las distintas acciones que
    tenemos disponibles 

    METODOS/CLASES:

            "Una clase es como un molde para crear objetos. Es una forma de agrupar datos (llamados atributos)
                         y acciones (llamadas métodos) que tienen algo en común y que tiene: 
                         Atributos: Son las características del objeto. Por ejemplo, un auto tiene color, marca y velocidad
                         Métodos: Son las acciones que el objeto puede hacer. Por ejemplo, un auto puede arrancar, frenar o doblar"

            requests.get --> Es una clase, que nos sirve para darnos la repsuesta que nos da el servidor cuando hacemos el pedido 
            .json --> el archivo con el cual vamos a laburar
                                                                            
      """
def main():

    api_key = "0L7EQWQLYVQNJWJR"
    simbolo = "AAPL"
    datos = obtener_datos(api_key, simbolo)
    guardar_json(datos, "datos_bolsa.json")
    print("Datos guardados en 'datos_bolsa.json'")
    mostrar_ultimo_cierre(datos)

main()
