# Ejercicio 2	
# Escriba un programa que ingrese (por teclado) los datos de diez personas 
# (nombre, edad, genero, dirección, teléfono), 
# los almacene en un diccionario y los muestre. 
# Al realizar dicha muestra, destacar la persona más joven en edad.

# SOLO 2 PERSONAS

print("************* Ingrese los datos de 2 personas *************")
personas = []

while len(personas) <= 2:
    dato={}
    dato["nombre"] = input("Ingrese un nombre: ")
    dato["edad"] = int(input("Ingrese una edad: "))
    dato["genero"] = input("Ingrese un genero: ")
    dato["direccion"] = input("Ingrese una direccion: ")
    dato["telefono"] = input("Ingrese un telefono: ")

    personas.append(dato)

print("****** Datos de la persona ******")   
for dato in personas:
    print(f"nombre{dato["nombre"]} edad{dato["edad"]} genero{dato["genero"]} direccion{dato["direccion"]} telefono{dato["telefono"]}") 


