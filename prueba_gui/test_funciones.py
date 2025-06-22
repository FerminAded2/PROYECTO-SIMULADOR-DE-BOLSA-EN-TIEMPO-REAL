import unittest #Al parecer traer unittest no sirve para invocar patch
from unittest.mock import patch #Es un submoludo, por lo cual hay que traerlo de esta forma
from simulacion_de_datos import pide_datos_del_usuario as pd
from simulacion_de_datos import crea_matriz


def documento():

    """
    -------------------------------------------------------------------------------------------

    - - FUENTE - - Los datos fueron tomados de :

    https://docs.python.org/es/3/library/unittest.html?utm_source=chatgpt.com#unittest.main

    --------------------------------------------------------------------------------------------

    Se pueden ejecutar las pruebas con más nivel de detalle (mayor verbosidad)
    pasando el parámetro -v:
    
    || python -m unittest -v test_module || en nuestro caso :
                    |
                    |
                    V
        python -m unittest -v test_funciones  
        
    -----------------------------------------------------------------------------------------------------------
    El siguiente bloque de codigo fue VISTO EN CLASE:

    import os

    | ruta_actual = os.path.dirname(__file__)                     |
    | ruta_completa = os.path.join(ruta_actual, "archivo.py")     |

            ------------------------------------

                - - - IMPORTANTE - - -

    PREGUNTA
    podemos usarlo para importar un modulo, haciendo LO VISTO EN CLASE de archivos ???

    Al parecer no, pero hay que consultar, supuestamente se hace lo siguiente:

    import sys
    import os

    # Agrego el directorio padre a sys.path
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))

    from simulacion_de_datos import pide_datos_del_usuario, crea_matriz

    y con esto no habria probelmas para que se encuentre nuestro .py de donde tomamos las funciones
    las cuales vamos a probar, en este caso del archivo .py -- > "simulacion_de_datos" 

    """

def test_pide_datos_del_usuario():
    with patch("builtins.input", side_effect=["Emiliano", "veinte", "22"]): #con esto simulamos entrada
        nombre, edad = pd()
        assert nombre == "Emiliano"
        assert edad == 20

def verifica_largo ():
    
    esperado = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ] 

    largo_esperado=len(esperado)
    
    return largo_esperado
    
    resultado = crea_matriz()
    assert resultado == esperado


def main():
    documento() 
    test_pide_datos_del_usuario()
    verifica_largo()

    if __name__=="__main__" :

        unittest.main()

"En terminal poner:  python -m unittest -v test_funciones"


