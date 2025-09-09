numeros=[0,1,2,3]

listaVariada=["Oliver",55,66,6.39]

print(listaVariada[3])

print(listaVariada[-2])

print(listaVariada)
listaVariada.append("Curso de Python")
print(listaVariada)


listaNombres=["Juan","Jose"]

listaNombresTarde=["Pedro","Antonio"]

listaCompleta = listaNombres + listaNombresTarde

print(listaCompleta)

listaCompleta[0]="Guido"

print(listaCompleta)

del listaCompleta[2]

print(listaCompleta)

listaLetras=['a','b','c','a','t','y']
print(len(listaLetras))
listaLetras.remove('a')

print(listaLetras)

listaLetras.pop(1)

print(listaLetras)

listaLetras.clear()

print(listaLetras)

print(len(listaLetras))

for i in range(len(listaCompleta)):
    print(listaCompleta[i],end=",")

frutas=["banana","pera","manzana","frutillas"]

# in y not in 
print()

if 'mani' not in frutas:
    print("El mani esta en la lista")

n1=10
n2=33
n3=45

#Empaquetado 
listaNumeritos=[n1,n2,n3]

diasDeLaSemana =["Lunes","Martes", "Miercoles"]


#Desempaquetado
primerDia, segundoDia,tercerDia = diasDeLaSemana

print(primerDia)
print(segundoDia)

computadoras=["Lenovo"]

computadoras=computadoras*4

print(computadoras)