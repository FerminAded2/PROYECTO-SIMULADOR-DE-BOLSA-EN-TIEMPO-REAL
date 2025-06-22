import unittest
from simulacion_de_datos import crea_matriz

#para comprobar si la matriz se crea correctamente abrir carpeta de prueba_gui y ejecutar python "test_simulacion.py" en la terminal

class TestSimulacionDeDatos(unittest.TestCase):
    def test_crea_matriz_es_4x4(self):
        matriz = crea_matriz()
        self.assertEqual(len(matriz), 4)  # Verifica 4 filas
        for fila in matriz:
            self.assertEqual(len(fila), 4)  # Verifica 4 columnas por fila

if __name__ == "__main__":
    unittest.main()
