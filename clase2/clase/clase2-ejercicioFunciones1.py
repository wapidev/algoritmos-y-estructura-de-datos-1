"""Desarrollar una función que reciba tres números enteros y devuelva el mayor de los tres. Devolver -1 en caso de existir igualdad. 
Desarrollar un programa principal que invoque a la función, en el programa principal solicitar los datos al usuario"""

def calcular_maximo(numero1,numero2,numero3):
    if numero1==numero2 and numero2==numero3:
        return -1
    else:
        maximo=max(numero1,numero2,numero3)
        return maximo 


num1=int(input("Ingrese el primer numero"))
num2= int(input("Ingrese el segundo numero"))
num3= int(input("Ingrese el tercer numero"))

print("El maximo es ",calcular_maximo(num1,num2,num3))