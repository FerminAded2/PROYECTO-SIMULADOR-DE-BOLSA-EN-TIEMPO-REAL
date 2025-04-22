import random
import json
import os # Para ver el contenido del json 
          # solo para este caso 

#--------------------------SECCION_00----------------------
def pide_datos_del_usario():

    "Enpaquetado y desenpaquetado de datos de la llamda a la funcion"

    nombre=input("Escriba su nombre: ")
    edad=int(input("Ingrese su edad: ")) 

 #Podemos poner que la persona solo pueda ingresar un dato alfabetico 
    #Y hasta que eso no pase, que se siga pidiendo el dato 

#----------------------------------------------------------             

    return nombre,edad
             
               

def crea_matriz():
    "Crea la matriz con dato de las acciones"
    
    columnas=4
    filas=4
    matriz=[[0 for c in range(columnas)] for f in range (filas)] 
    # Asi como se puede hacer listas por compresion, podemos hacer
    # Matrices(listas de listas) por compresion 

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

    #IMPORTANTE-LEER EN DOCUMENTO
    for elementos in matriz:
        print (elementos)

    print ()    

    print ("El promedio de las acciones en el dia(en este caso es se toma 4 veces)")
    for fila in resultado:
        print (f"{fila[0].upper()}  --> {fila[1]} --> Precio promedio ")

        # uso upper para pasar todo el texto a mayuzcula

def armamos_dic(tupla):

    diccionario={}

    for dato in tupla :
        empresa=dato[0] #Recordemos que las empresas estan en el indice 0 de la tupla
        precio=dato[1]
        diccionario[empresa]=precio

    #---------------explicacion_en_documento----------------------------------
    #---------------  JSON ---------------------------------------------------

    with open ("Promedio_de_acciones","w") as archivo: #write (escribir) como no existe,hay que escribir el archivo
        json.dump(diccionario,archivo,indent=4)
        os.startfile("Promedio_de_acciones")

    return diccionario



def documento():

   
    """

    IDEA: 
    La idea de este .py es tener un simulador de datos, los cuales en un 
    futuro seran tomados por una API que nos dara los precios de las acciones
    del mercado bursatil EN TIMEPO REAL. Para esto se implementa todos los temas vistos hasta 
    la clase del 21/04. 

    --------------------------SECCION_01-----------------------------------

    POR QUE NO PODEMOS USAR EN LA FUNCION "RELLENAR"
    UN APPNED EN LA MATRIZ. ej 
    
        matriz[f][c].append(random.randint(1,10000))

    Explicacion = .append(...) se usa solo con listas
                 pero cada celda es un int o str, no una lista 
                 por eso no se puede.
                 Por algun motivo, no se accede a la celda, sino
                 al numero dentro de esa celda, por lo cual no se le 
                 puede agregar un dato a un numero. sino 
                 miremos lo siguiente:

                 ponele que matriz[0][1] = 20 ;ahi tenemos el 20 en [0][1]
                 entonces... ? 
                 bueno entonces eso se ve algo como esto...

                 -------> 20.append(random.randint(1,1000))
                y visto asi tiene mas sentido que no sea valido, asi que con 
                un simple cambio como el siguiente, podems tener lo que queremos
                que seria:
                
                matriz[0][1]=random.randint(1,10000) 

                esto mete el dato dentro de la posicion y no dentro del numero
        ----------------------------------------------------------------------------------
        -------------------------------------------------------------------------

     for elementos in matriz: --------> SI NOS OLVIDAMOS Y PONEMOS--> for elementos in matriz():

     el " ( ) " es decir los PARENTISIS;
     MATRIZ sera tomado como un objeto y nos dara un error en el programa, por eso va sin los parentesis

     ---------------------------------------------------------------------------------------------------
    #---------------  JSON ---------------------------------------------------

    .OPEN --->abris un archivo ("Promedio_de_acciones","w")
                                                        |
    ----------------------------------------------------                                                    
    |
    V

    W --- > viene de write (escribir) es como append pero en este caso 
            usamos W cuando no existe el archivo, se podria decir que lo "inicialiazamos"
            no se si es la palabra correcta, pero seria algo por el estilo 
            

    AS --- > es como en base de datos, cuando escribos as y cambiamos el nombre

    json.dump ---> asi como en lambda tenemos este formato (<argumento>:<exprecion>) en este caso tenemos 

                    json.dump(<objeto_de_python>,<archivo_abieto>,<opciones>)

                    objeto_de_python --> diccionario,tuplas,listas 
                    archivo_abieto ----> el archivo donde vamso a guardar los datos
                    opciones ---------> con lo que le  damos formato, con indet le damos los saltos de linea y
                                        un formato mas prolijo 

    """ 
    pass
                    
#Codigo_principal

def main ():

    nombre,edad=pide_datos_del_usario()

    print(f"El nombre del usurio es: {nombre} y su edad: {edad} años")

    matriz=crea_matriz()
    
    empresas=nombres_de_empresas()

    matriz_con_datos_01=rellena(matriz,empresas)

    resultado=list(map(lambda fila:(fila[0],sum(fila[1:])/4),matriz))
    
    convertido_a_tupla=(tuple(resultado)) #Implementacion_de_tuple al "resultado"

    covertimos_tupla_a_diccionario=armamos_dic(convertido_a_tupla)



    impresion(matriz_con_datos_01,resultado)

    documento()

main()
