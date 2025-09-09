# Leer un conjunto de números enteros, calcular su
# promedio e imprimir aquellos que superan el promedio

# Ejercicio 1

cantNumeros = int(print('Ingresa la cant de números'))
listaNumeros=[]
for i in range(listaNumeros):
    numero=int(print('Ingrese un número:'))
    listaNumeros.append(listaNumeros[i])

promNumeros = sum(listaNumeros)/cantNumeros

print('Números que superan el promedio')

for i in range(listaNumeros):
    if listaNumeros[i] > promNumeros:
        print(listaNumeros[i],end='-')


