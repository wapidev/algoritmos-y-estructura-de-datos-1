"""
Crear una función que reciba una lista como parámetro. 
Dentro de la función, crear una nueva lista y 
asignarla a la variable original. 
Imprimir los IDs de ambas listas antes y 
después de la asignación dentro de la función. 
¿Qué puedes concluir sobre el comportamiento de Python en este caso?
"""

def funcion(lista):
    print("Id antes de la modificacion ",id(lista))
    lista=id(lista)
    print("Id despues de la modificacion ",id(lista))


listita=[1,2,3]

print("El id de la lista fuera de la funcion es ",id(listita))

funcion(listita)

print(id(listita))

listita.append(5)
print(id(listita))