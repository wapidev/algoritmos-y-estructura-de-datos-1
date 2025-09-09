"""
8.	Crear una función que reciba dos números enteros como parámetros. Ambos valores recibidos 
como parámetros se deben modificar. Imprimir los IDs de ambos números antes, 
durante y después de la llamada a la función. 
¿Cuál es la relación entre los IDs antes y después de la llamada a la función?
"""

def funcion(numero1,numero2):
    print("Id dentro de la funcion numero1 antes de modificarlo",id(numero1))
    print("Id dentro de la funcion numero2 antes de modificarlo",id(numero2))
    numero1+=1
    numero2+=2
    print("Id dentro de la funcion numero1 despues  de modificarlo",id(numero1))
    print("Id dentro de la funcion numero2 despues de modificarlo",id(numero2))

numerito1=10
numerito2=20

print("El id de numerito 1 por fuera de la funcion es ",id(numerito1))
print("El id de numerito 2 por fuera de la funcion es ",id(numerito2))

funcion(numerito1,numerito2)