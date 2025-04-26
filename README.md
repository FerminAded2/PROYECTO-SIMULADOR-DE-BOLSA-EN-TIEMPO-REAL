# Simulador de Bolsa en Tiempo Real

Grupo N°2  
Integrantes: Aded Fermin, Leiva Emiliano, Palacios Imanol, Storni Felipe


# OBJETIVO  
El objetivo del proyecto es realizar un simulador de la bolsa de valores y de esta forma poder brindar una herramienta que permita introducirse a la actividad de vender y comprar activos sin riesgo de perder dinero.


# FUNCIONALIDADES  
Las funcionalidades del sistema serán vender y comprar acciones con dinero ficticio. Los precios de las acciones serán reales gracias a la API de Alpha Vantage y se actualizarán 5 veces por minuto durante un lapso de 10 minutos. Una vez finalizados los 10 minutos se mostrara el resultado de las ganancias o perdidas segun el rendimiento del usuario.


# ENTREGABLES  

# 40%  
- Redaccion del SRS del proyecto.  
- Creación del repositorio en GitHub y redaccion del archivo README.md.  
- Implementacion de una interfaz gráfica básica usando Tkinter.
- Simulador de datos (simula a la API).  
- Uso de archivo JSON para guardar los datos.

# 80%  
- Funcionalidades para compra y venta de acciones segun el dinero disponible.  
- Registro del portafolio del usuario mediante diccionarios de Python.  
- Implementacion de un DAG de Apache Airflow que actualiza precios 5 veces por minuto consultando la API con requests y guarda los datos en JSON.  
- Implementacion de un cronometro de 10 minutos para cada partida usando la libreria time.
- Integracion con Alpha Vantage usando la libreria requests.
  
# 100%  
- Desarrollo de la pantalla final donde se muestra ganancia o perdida.  
- Calculo final sumando el dinero disponible y el valor actual del portafolio.  
- Visualizacion de resultados extrayendo los datos desde los archivos JSON.


