"""2.	Escriba un programa que lea datos de tres personas 
(nombre, edad, genero, dirección, teléfono), los almacene en 
un diccionario y los muestre. Al realizar dicha muestra, 
destacar la persona más joven en edad."""

# SOLO 2 PERSONAS   

print("************* Ingrese los datos de 2 personas *************")
personas=[]
while len(personas)<=2:
    dato={}
    dato["nombre"]=input("Ingrese un nombre: ")
    dato["edad"]=int(input("Ingrese una edad: "))
    dato["genero"]=input("Ingrese un genero: ")
    dato["direccion"]=input("Ingrese una direccion: ")
    dato["telefono"]=input("Ingrese un telefono: ")

    personas.append(dato)   

print("****** Datos de la persona ******")   
for dato in personas:
    print(f"nombre: {dato['nombre']} edad: {dato['edad']} genero: {dato['genero']} direccion: {dato['direccion']} telefono: {dato['telefono']}")

# Buscamos la persona mas joven
menor=personas[0] # Variable para acumular la persona más joven
for dato in personas:
    if dato['edad']<menor['edad']: #Tomo el primer elemento como el menor y voy comparando
        menor=dato
print("La persona más joven es:")
print(f"nombre: {menor['nombre']} edad: {menor['edad']} genero: {menor['genero']} direccion: {menor['direccion']} telefono: {menor['telefono']}")