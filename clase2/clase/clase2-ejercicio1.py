#Leer un conjunto de números enteros, calcular su promedio e imprimir aquellos que superan el promedio

cantNumeros= int(input("Ingrese la cantidad de numeros que desea leer"))
listaNumeros=[]

for i in range(cantNumeros):
    numero= int(input("Ingrese un numero"))
    listaNumeros.append(numero)

if cantNumeros>0:
    promedio=sum(listaNumeros)/cantNumeros

print("Numeros que superan el promedio")

for i in range(len(listaNumeros)):
    if listaNumeros[i]>promedio:
        print(listaNumeros[i],end="-")