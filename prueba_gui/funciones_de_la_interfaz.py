
import tkinter as tk  # -- Lo renombramos asi porque es el consejo que se nos da el la pagina oficial
from PIL import Image, ImageTk# baiscamente laburamos con imagnes. Voy a ampliarlo en el docmuento 
import os # -- > Sirve para que se cargue la imagen correctamente

def datos_del_tiempo ():
    
    """
         contiene informacion basica del programa #TIEMPO

        --- por que lo puse de esta froma ? ---
        para que sea mas facil de identificar si se 
               quiere cambiar un paramtro 

    """

    t=10            # ACA SE AUMENTA O DISMINUYE EL TIEMPO DEL JUEGO

#---------------------------------------IDEA -------------------------------------------------------------- 
    #  
    #      - Podemos hacer una pantalla de inicio, con el TITULO del juego

    #      - Luego un segundo titulo mas chico en la parte de abajo que diga INICIAR 

    #      - Por ultimo dar a elegir al usuario cuanto tiempo quiero jugar con 3 opciones 
    #        que seran botones, una opcion dara 10 minutos (que es el minimo) luego dara 20 
    #        y por ultimo, la opcion que le dara abre una ventana pequeña, un campo 
    #        (un renglon)
    #        donde escribe cuanto tiempo desea jugar.
     
    #       > PORQUE CREO QUE ES BUEAN IDEA ESTO :

    #       1- podemos trabajar con EXCEPCIONES - decirle al usuario que meta un numero
    #                                             de caso contrario, se le sigue pidiendo
    
    #       2 -Podemos trabajar el metodo visto en clase .lower o .upper para copnvertir
    #          lo que escriben por teclado, como mayuscula o miniscula 
      
#--------------------------------------------------------------------------------------------------------         
      
    
        
    minutos_total= t*60 # Minutos_total contine los segundos en el total de minutos

    return minutos_total 


#=================================== SECCION 1 ==========================================================================

def iniciamos_cronometro(label,minutos_total,tiempo_actual=0):  # El label es un metodo de tkinter, una etiqueta
    """
    Aca esta la magia de todo el funcionamineto del cronometro,
    en la docmunetacion esta todo explicado, pero basicamenten vamos 
    a usar recursividadad para que nuestro cronometro ande
    IMPORTANTE: NO SE USA BUCLES PORQUE NON SE PUEDE CON ESTA LIBRERIA 

                  ---  SE EXPLICA T-ODO EN EL DOC ----
    
    """

    
    
    if tiempo_actual<=minutos_total: # Tiempo total arranca en cero. Esto es importante 
                                     # como veremos en las lineas de codigo mas abajo 
        
        minutos=tiempo_actual//60    #

        segundos = tiempo_actual % 60 #con el moduilo vemos el resto 
        
        # metodo f_string = https://docs.python.org/3/reference/lexical_analysis.html#f-strings 

        formato_del_texto = f"{minutos:02}:{segundos:02}" # Le damos formato de reloj 
        #  ------> que significa ? :
        # |                     " : " --- > le damos un formato determinado al numero
        # |                     " 02 " --- > Con esto le decimos...che queremos 2 cifras
        # |
        # v                                  si falta   una, se le agrega una a la izquierda                                   
        
        label.config(text=f"Tiempo: {formato_del_texto}") # Mostramos el tiempo en la etiqueta
        # |
        # |
        # v

        #La explicacion de porque es asi se encuentra en documento>metodos>.after


        label.after(1000, lambda: iniciamos_cronometro(label, minutos_total, tiempo_actual + 1))

    else:
           
        label.config(text="¡Cronómetro finalizado!")   # Si el tiempo llegó a más de 10 minutos, 
                                                       # mostramos el mensaje final  

#============================================================================================================

def documento ():

    """  IDEA : 
    
        La idea del doumento es... valga la redundancia, documentar todo. Con la finalidad 
        de que quede un registro de todo lo realizado, y quede bien claro como se encaro 
        el codigo en cada apartado, para esto se uso el material proporcionado en clase,
        (ya que es de donde mas herramientas sacamos para poder comprender lo que estabamos
        haciendo) ademas de la documentacion ofical de python en la que podemos encontrar 
        el funcionamiento de la libreria usada en este proyecto """
    
    """ LINK = https://docs.python.org/es/3.13/library/tkinter.html """
    
    """ SINTAXIS - ESTRUCTURA DEL CODIGO :

        NOTACION A USAR ------->  Notación snake_case (separo las palabras con un un "_" )

        ENCABEZADO/COMENTARIO --> " -------------- LO QUE SEA -------------------------- "
        
                        TAMBIEN SE HARAN COMENTARIOS DE FUNCIONES/METODOS/VARIABLES 
                        Y T-ODO AQUELLO QUE PUEDA DAR A CONFUCIONES

                        ESTO SE VERA COMO:
                                            VEHICULO=ALGO # VEHICULO SE LLAMA ASI PORQUE 
                                            TIENE 4 RUEDAS
                                            ES UN EJEMPLO SENCILLO DE COMO PODRA VERSE  

    """

    """   CRONOMETRO: 
        
        tkinder no puede usar un buble para algo como un cronometro ya que su uso 
        hara que la interfaz se congele, se puede usar threading pero esto no nos salva
        de no tener  ningun tipo de problemas en un futuro. Por lo cual, con lo anteriormente
        dicho, la estrategia para realizar esta parte del codigo, sera la de usar una funcion
        recursiva. Entonces con la funcion recursiva llamaremos a la misma funcion, y con esto
        podemos avanzar, algo asi como la variable que esta dentro del bucle for, que 
        normalmente (en fundamentos de informatica) la vemos como for i in range, la 
        i (variable que nosostros elegimos) aumenta o decrece segun le indiquemos, de forma 
        automatica. Para la funcion recursiva seguiremos la misma idea, pero obvimente de una
        forma distinta. Tendremos que usar metodos de la libreria mencionada (tkinder). 
        Todo lo mencionado anteriormete es lo que se ve en el codigo  

    """
    """ METODOS : 

        .LABEL --- > es una etiqueta de texto de tkinter, como si fuera un cartel en ventana
                     En este caso la vamos a usar para mostrar el cronometro 

                     label=tk.label (ventana, fron=("arial",24))

                     luego debemos modificar la etiquieta, para actualizar el texto
                     que en este caso seria el numero. Esto lo pense como una referencia
                     a un objeto en POO, en el paradigma que acabo de nombrar SELF 
                     representa el objeto en si mismo, label en este caso es una instancia 
                     puntual de la libreria Tkinter (la idea puede no estar del todo bien, hay 
                     que corroborarlo, pero yo lo pense asi no se)

        .CONFIG -- > Este metodo sirve para modificar el contenido del texto que se muestra por
                     pantalla

        .AFTER --- > El metodo se "comunica" (no se si es la palabra exacta )
                    con la ventana, entonces le manda instrucciones, y le dice... che, mira
                    que se para en x tiempo, entonces espera ese x tiempo y depues arranca 
                    de nuevo.En el codigo que hicimos se usa con una funcion lambdam la cual 
                    dsp de cada segundo, le dice que arranquem entonce spor cada vez que no 
                    se cu mpla con la condicion se hace una iteracion, como en un bucle for

                    un detalle --- > ventana.after(1000, funcion) 
                                            (<parametro_01>,<funcion>)
                    
                    parametro_01 = en MILI SEGUNDOS, esto es asi porque fue heco de esta manera
                                   por eso, en vez de poner 1 (segundo) ponemos 
                                   1000(milisegundos)= 1 segundo


    |-------------------------#PILLOW----------------------------------------------------------||

        IDEA: Estoy pensando que tal vez hacer la interfaz con cosas que llamen la atencion, como
        colores o imagenes con personajes, haria que se le preste mas atencion a lo que se ve por pantalla. 
        Ya que estamos trabajando con una interfaz que se ve muy sencilla, como un S.O viejo, tal 
        vez podriamos usar eso a nuestro favor usando una estetica de pixel art con imagenes divertidas
        que aparezcan al hacer acciones/consecuensias es decir, nosotros compramos nos aparece una carte
        de un personaje con una bolsa de plata, vendemos aparece otra cosa, perdemos plata nos aprece el
        personaje triste y asi para cada cosa. Esto llamaria la atencion del usurio y haria mas llevadera 
        la experencia de uso del programa. 
         
        Entonces para hacer lo que acabo de proponer, podemos usar pillow, la pirmera imagen que seria nuestra
        prueba piloto, seria un reloj de arena que se encuentra al lado del cronometro. Luego el segundo paso
        seria agregar a las acciones/consecuencia imagenes. Me gustaria que la interaccion sea la siguiente:
        el Usuario apreta un boton. Ej boton compra, una vez hecho esto, el usario ve una carta del personaje,
        lo que estaria pasando dentro del codigo seria que abrimos una ventana que contiene una imagen, esta se 
        presenta por pantalla algunos segundos y luego deja de verse. Para todo lo dicho, como dije anteriormente
        podemos usar pillow, el tema de como sera el apartado visual en cuanto transiciones de cartas es algo 
        que todavia tenemos que ver 
        
        link=https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.resize  ||

    |    .iMAGE ---> Nos deja abrir la imagen (el .png)                                        ||
    |                                                                                          ||
    |   .IMAGETK --> hace que la imagen sea compatible con tkinder                             ||

    |   .RESIZE ---> Con esto se hace una nueva imagen cion las dimensiones                    ||
                    que le pasamos en (ancho,alto)
    |   
        .OPEN ----. > Abris la imagen                                                          ||
    
    ______________________________________________________________________________________________

       FUNCION LAMBDA --- > lamda <parámetro>: <expresión que devuelve>
                           
                            ej : lambda x: x**2 ----> te da todo los x al cudrado 

        


                                                                                        
    """

    # Luego podemos analizar si armar un .py con documentacion para que quede mas prolijo
    # o meterlo en Github, con un Readme (consultar con la profe )


# Programa principal 

def main ():
    """En esta seccion tendremos todas las llamadas de las funciones"""

    minutos_total=datos_del_tiempo()

    # ---------------------------------CONSULTA----------------------------------------------------
    """ 
        consulta --> deberia ir todo lo que esta contenido
                     entre comentarios --- ,en el PROGRAMA PRINCIPAL 
                     o habria que ponerlo en otro lado, para no
                     cometer una mala practica de progrmacion ??? 

    """
    
    ventana=tk.Tk()
    ventana.title("Simulador de bolsa en tiempo real") # este sera el titulo que pondremos
    ventana.config(bg="#dceefb") #El color de la ventana
    
    # Etiqueta del cronómetro
    label_cronometro = tk.Label(ventana, text="Tiempo Restante: 10:00", font=("Arial", 16), bg="#dceefb")
    label_cronometro.grid(row=0, column=1)

    ruta_absoluta = os.path.join(os.path.dirname(os.path.abspath(__file__)), "reloj_de_arena.png")
    imagen_original=Image.open(ruta_absoluta)
    imagen_reducida=imagen_original.resize((48,60))
    imagen_tk = ImageTk.PhotoImage(imagen_reducida)
    


    label_imagen=tk.Label(ventana, image=imagen_tk, bg="#dceefb")
    label_imagen.image=imagen_tk  # evitar que se libere la imagen de memoria
    label_imagen.grid(row=0,column=2, padx=10) # justo al lado derecho del cronómetro

    # Creamos un botón que va a iniciar el cronómetro cuando lo apretemos
    boton = tk.Button(ventana, text="Iniciar", command=lambda: iniciamos_cronometro(label_cronometro, datos_del_tiempo()))
    boton.grid(row=1, column=1, pady=10)
    
    #-----------------------------------------------------------------------------------------

    documento() #acordate que si queres ver la documentacion, por terminal, help(documento)

    # Iniciamos la ventana para que se mantenga abierta
    ventana.mainloop()
    if __name__ == "__main__":
        # Si el script se ejecuta directamente, llamamos a la función main

        main ()

