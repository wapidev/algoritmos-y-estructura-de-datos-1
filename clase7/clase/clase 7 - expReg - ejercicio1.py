#Escribir un programa que busque la palabra celular en una cadena 
#ingresada por el usuario. 

import re

palabra = input("Ingresa una frase ")

patron="celular"

# Paso 1, basico
if re.search(patron,palabra,re.IGNORECASE):
    print("La palabra celular se encuentra")


# findall para obtener la lista de cadenas que encontro, y devuelve como una lista
palabrasEncontradas=re.findall(patron,palabra,re.IGNORECASE)
print(palabrasEncontradas)

# Ejemplo con len
print(len(palabrasEncontradas))

# print(palabrasEncontradas[0])
