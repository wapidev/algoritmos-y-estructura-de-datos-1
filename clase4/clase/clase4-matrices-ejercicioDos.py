"""
Crea una matriz con un tamaño que el usuario le indique por teclado (puede ser 6×4, 7×2, etc.) pero como máximo podrá contener 10x10 valores y como mínimo 2x2. Crear una función para la cargar de los valores y, por último, otro procedimiento para visualizar los resultados. Los valores para cargar deberán ser número positivos entre 0 y 100, siendo éstos generados al azar."""

import random

def cargarMatriz(filas, columnas):
    matriz=[]

    for i in range(filas):
        fila=[]

        for j in range(columnas):
            numero= random.randint(0,100)
            fila.append(numero)
        matriz.append(fila)

    return matriz

def mostrarMatriz(matriz):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            print(matriz[fila][columna], end="-")
        print()

cantFilas = int(input("Ingrese la cantidad de filas que va a tener su matriz"))
cantColumnas = int(input("Ingrese la cantidad de columnas que va a tener su matriz"))

if cantFilas<2 or cantColumnas<2 or cantFilas>10 or cantColumnas>10:
    print("Cantidad de columnas y filas invalidas")
else:
    matrizCargada = cargarMatriz(cantFilas,cantColumnas)
    mostrarMatriz(matrizCargada)
