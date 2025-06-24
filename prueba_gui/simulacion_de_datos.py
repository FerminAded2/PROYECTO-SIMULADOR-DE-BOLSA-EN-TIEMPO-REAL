import random
import json
import os
import time

# ---------------- RECURSIVIDAD APLICADA ----------------
def contar_chistes(chistes, i=None):
    if i is None:
        i = len(chistes) - 1  # empieza desde el ultimo
    if i < 0:
        return
    print(f"Chiste {len(chistes) - i}: {chistes[i]}")
    contar_chistes(chistes, i - 1)

#--------------------------SECCION_00----------------------
def pide_datos_del_usuario():
    condicion=False
    while not condicion:
        nombre=input("Escriba su nombre: ")
        try:
            edad=int(input("Ingrese su edad: ")) 
            condicion=True
        except ValueError:
            print ("Por favor, ingrese un numero")
    return nombre,edad 

#----------------------------------------------------------                   

def crea_matriz():
    columnas=4
    filas=4
    matriz=[[0 for c in range(columnas)] for f in range (filas)] 
    return matriz

def nombres_de_empresas():
    nombres=["samsung","IBM","Mercado_libre","Amazon"]
    return nombres 

#--------------------------SECCION_01----------------------

def rellena(matriz,empresas):
    filas=len(matriz)
    columnas=len(matriz[0])
    for f in range (filas):
        for c in range(columnas):
            if c==0:
                matriz[f][c]=empresas[f]
            else :
                matriz[f][c]=random.randint(1,10000)
    return matriz 

def impresion(matriz,resultado):
    for elementos in matriz:
        print (elementos)
    print ()    
    print ("El promedio de las acciones en el dia(en este caso se toma 4 veces)")
    for fila in resultado:
        print (f"{fila[0].upper()}  --> {fila[1]} --> Precio promedio ")

def armamos_dic(tupla):
    diccionario={}
    try :
        for dato in tupla :
            empresa=dato[0]
            precio=dato[1]
            diccionario[empresa]=precio
    except IndexError:
        print("Error: La tupla no tiene el formato esperado (empresa,precio)")
        return None
    except Exception as e:
        print("Error al procesar los datos:",e)
        return None
    try:
        ruta_json = os.path.join(os.path.dirname(__file__), "Promedio_de_acciones.json")
        with open (ruta_json,"w") as archivo:
            json.dump(diccionario, archivo, indent=4)
        try:
            os.startfile(ruta_json)
        except Exception as e :
            print ("No se puede abrir el archivo automaticamente:",e)
    except Exception as e:
        print("Ocurrio un error al guardar el archivo JSON:", e)
        return None
    return diccionario

#----------------------------- Seccion terminal ------------------------------

def mostrar_portafolio(saldo, portafolio):
    print()
    print("----- TU PORTAFOLIO -----")
    print("Saldo disponible:", saldo)
    for empresa, dinero in portafolio.items():
        print(empresa, ": $", dinero)
    print("-------------------------")

def invertir(empresa, monto, saldo, portafolio):
    if monto <= saldo:
        saldo -= monto
        portafolio[empresa] += monto
        print(f"Invertiste ${monto} en {empresa}")
    else:
        print("No tenes saldo suficiente")
    return saldo

def retirar(empresa, monto, saldo, portafolio):
    if portafolio[empresa] >= monto:
        saldo += monto
        portafolio[empresa] -= monto
        print(f"Retiraste ${monto} de {empresa}")
    else:
        print("No tenes ese monto invertido en", empresa)
    return saldo

def mostrar_empresas(empresas):
    for i, empresa in enumerate(empresas):
        print(i, "-", empresa)

def elegir_empresa(empresas):
    mostrar_empresas(empresas)
    return input("Elegir empresa por numero o -1 para salir: ")

def pedir_monto():
    try:
        return int(input("Cuanto dinero: "))
    except ValueError:
        print("Monto invalido")
        return None

def procesar_accion(empresa, saldo, portafolio):
    accion = input("Invertir o retirar i/r: ").lower()
    if accion not in ["i", "r"]:
        print("Opcion no valida")
        return saldo
    monto = pedir_monto()
    if monto is None:
        return saldo
    if accion == "i":
        saldo = invertir(empresa, monto, saldo, portafolio)
    elif accion == "r":
        saldo = retirar(empresa, monto, saldo, portafolio)
    return saldo

#----------------------------- Seccion terminal - principal ------------------------------

def interaccion_con_terminal(empresas):
    saldo = 10000
    portafolio = {empresa: 0 for empresa in empresas}
    inicio = time.time()
    condicion = False
    while not condicion:
        if time.time() - inicio >= 600:
            print("Tiempo agotado")
            condicion = True
        elif saldo == 0:
            print("Ya no tenes saldo disponible para invertir")
            condicion = True
        else:
            mostrar_portafolio(saldo, portafolio)
            entrada = elegir_empresa(empresas)
            if entrada == "-1":
                print("Fin del programa")
                condicion = True
            else:
                try:
                    indice = int(entrada)
                    if 0 <= indice < len(empresas):
                        empresa = empresas[indice]
                        saldo = procesar_accion(empresa, saldo, portafolio)
                    else:
                        print("Empresa invalida intenta de nuevo")
                except ValueError:
                    print("Entrada invalida")
    print()
    print("Programa finalizado")
    mostrar_portafolio(saldo, portafolio)

#---------------Codigo_principal--------------------------------------------------------------

def main ():
    nombre,edad=pide_datos_del_usuario()
    print(f"El nombre del usurio es: {nombre} y su edad: {edad} anos")
    matriz=crea_matriz()
    empresas=nombres_de_empresas()
    matriz_con_datos_01=rellena(matriz,empresas)
    resultado=list(map(lambda fila:(fila[0],sum(fila[1:])/4),matriz))
    convertido_a_tupla=(tuple(resultado))
    covertimos_tupla_a_diccionario=armamos_dic(convertido_a_tupla)
    impresion(matriz_con_datos_01,resultado)
    interaccion_con_terminal(empresas)

    chistes = [
    "Por que Python no va al gimnasio? Porque ya tiene clases y objetos.",
    "Que hace un programador cuando tiene sueno? Ejecuta un thread y se duerme.",
    "Que hace una funcion recursiva cuando se queda sola? Se llama a si misma.",
    "Cual es el colmo de un programador? Tener un hijo con excepcion y no poder atraparlo."
    ]
    
    print("\nFin del simulador. Ahora, algunos chistes:")
    contar_chistes(chistes)

if __name__=="__main__":
    main()
