"""Desarrollar cada una de las siguientes funciones y escribir un programa principal que permita verificar el funcionamiento de las mismas
Cargar una lista con números al azar de cuatro digitos. La cantidad de elementos también debe ser ingresado por el usuario
Calcular y devolver el producto de todos elementos de la lista
Eliminar todos las apariciones de un elemento de la lista. No utilizar listas auxiliares. El elemento a eliminar se recibe por teclado
Determinar si una lista es capicua"""

import random
  
def cargarLista(cantidad):
    """Objetivo: Carga una lista al azar con 4 digitos
    parametro: cantidad: La cantidad de numeros a generar
    """
    lista = []
 
    for i in range (cantidad):
        num = random.randint(1000, 9999)
        lista.append(num)
    return lista
 
def main():
    cant = int(input("Ingresa la cantidad de elementos"))
    numeros = cargarLista(cant)
    print("La lista es:", numeros)

main()

[1,1,1,1,2,1,1,1,1]

def lista_capicua(lista):
 
    rango = len(lista) // 2 #4
 
    capicua = 0
 
    indice = -1
 
    for i in range(rango):
 
        if lista[i] == lista[indice]:
 
            capicua += 1
 
        indice -= 1
 
    if capicua == rango:
 
        print("La lista es capicua.\n")
 
    else:
 
        print("La lista no es capicua.\n")
 
 
numeros_capicua = [1,1,1,1,2,4,1,1,1,1]
 
lista_capicua(numeros_capicua)
 
numeros_no_capicua = [1,2,3,4,5,6,7]
 
lista_capicua(numeros_capicua)