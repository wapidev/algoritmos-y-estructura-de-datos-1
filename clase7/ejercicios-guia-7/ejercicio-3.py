# Ejercicio 3

# Hacer un programa que registre 10 alumnos y guarde: nombre, nombre de la asignatura y 4 notas. 
# Calcular y mostrar el promedio de las notas.

cantAlumnos = 3

alumnos = []

def calcularPromedio(notas):
    sumatoria = sum(notas.values)
    print("Promedio del alumno : ", sumatoria / len(notas))

while len(alumnos) <= 2:
    dato = {}
    notas = {}
    dato["nombre"] = input("Ingreso el nombre del alumno: ")
    dato["asignatura"] = input("Ingrese la asignatura: ")
    # dato["notas"]["nota 1"] = int(input("Ingrese la primero nota"))
    # dato["notas"]["nota 2"] = int(input("Ingrese la segunda nota"))
    # dato["notas"]["nota 3"] = int(input("Ingrese la tercera nota"))
    # dato["notas"]["nota 4"] = int(input("Ingrese la cuarta nota"))
    notas["nota1"] = int(input("Ingrese la primero nota: "))
    notas["nota2"] = int(input("Ingrese la segunda nota: "))
    notas["nota3"] = int(input("Ingrese la tercera nota: "))
    notas["nota4"] = int(input("Ingrese la cuarta nota: "))
    dato["notas"] = notas
    calcularPromedio(notas)
    alumnos.append(dato)

    # print(alumnos)
   



