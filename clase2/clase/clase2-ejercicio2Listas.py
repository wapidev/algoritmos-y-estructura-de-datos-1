"""
Escribir una función para ingresar desde el teclado una serie de números entre A
y B y guardarlos en una lista. En caso de ingresar un valor fuera de rango la función
mostrará un mensaje de error y solicitará un nuevo número. Para finalizar la
carga se deberá ingresar -1. La función recibe como parámetros los valores de A
y B, y devuelve la lista cargada (o vacía, si el usuario no ingresó nada) como
valor de retorno. Tener en cuenta que A puede ser mayor, menor o igual a B."""


def ingresoNumeros(limInferior,limSuperior):
    lista=[]

    minimo=min(limInferior,limSuperior)
    maximo=max(limInferior,limSuperior)

    bandera=True 

    while bandera:
        numero=int(input("Ingresa un numero"))

        if numero==-1:
            bandera=False
        else: 
            if numero>=minimo and numero<=maximo:
                lista.append(numero)
            else:
                print("Numero fuera de rango")
    return lista 

listaNumeros=ingresoNumeros(100,50)

print(listaNumeros)

print(min(50,50))
print(max(50,50))
