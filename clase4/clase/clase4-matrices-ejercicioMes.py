"""
Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4) y diga cuántos días tiene (por ejemplo, 30). Debes usar una matriz para su parametrización y una función para la recuperación del dato.
"""

def obtenerCantDiasMes(mes,matrizMeses):
    for i in range(len(matrizMeses)):
        if matrizMeses[i][0]==mes:
            return matrizMeses[i][1]


matricesMeses=[[1,31],
               [2,28],
               [3,31],
               [4,30],
               [5,31],
               [6,30],
               [7,31],
               [8,31],
               [9,30],
               [10,31],
               [11,30],
               [12,31],
               ]

mes= int(input("Ingresa el mes del que queres obtener la cantidad de dias"))


if mes<1 or mes>12:
    print("Numero de mes invalido")
else:
    print("El mes ", mes, "ingresado tiene", obtenerCantDiasMes(mes,matricesMeses), ' dias ')