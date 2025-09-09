#Declaracion de una funcion
def calcularProductoNumeros(numero1,numero2):
    """Objetivo: calcular la multiplicacion de dos numeros 
    """

    producto=numero1*numero2
    return producto

def esPar(numero):
    if numero%2==0:
        return True
    else:
        return False 
    
def decirHola():
    print("Hola")


print("Hola")
producto=calcularProductoNumeros(5,18)
print(producto)

print(decirHola())


#Tipos de datos mutables e inmutables 

numeroValor1=18
numeroValor2=39

calcularProductoNumeros(numeroValor1,numeroValor2)

#int, str, tuplas, float

def modificar_valor(x):
    x=10
    print("Valor de x adentro de la funcion ",x)

a=5
modificar_valor(a)
print("El valor de a luego de invocar a la funcion es ",a)

#Mutables - listas, diccionarios

def modificar_lista(lista):
    lista.append(59)
    print("La lista dentro de la función es ",lista)

miLista=[19,28,47]

modificar_lista(miLista)

print("Mi lista por fuera de la funcion ",miLista)

def verNumero():
    global numero
    numero=35



numero=20
verNumero()
print(numero)

help(calcularProductoNumeros)

help(min)