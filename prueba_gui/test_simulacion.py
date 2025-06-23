from simulacion_de_datos import crea_matriz

def test_matriz():
    matriz = crea_matriz()
    assert len(matriz) == 4  #verifica que hay 4 filas
    assert all(len(fila) == 4 for fila in matriz)  #verifica que cada fila tenga 4 columnas
