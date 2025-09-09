matrizAlumnos=[]

cantAlumnos = int(input("Ingresa la cantidad de alumnos que deseas cargar"))

for fila in range(cantAlumnos):
    alumno=[]

    nombre= input("Ingresa tu nombre ")
    legajo= input("Ingresa tu legajo ")

    alumno.append(nombre)
    alumno.append(legajo)

    matrizAlumnos.append(alumno)


for fila in range(len(matrizAlumnos)):
    print("Datos del alumno ")
    print("Nombre: ", matrizAlumnos[fila][0])
    print("Legajo: ",matrizAlumnos[fila][1])