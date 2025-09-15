#clave:valor
# Es una lista ordenada porque accedo por indices, pero en diccionario son clave-valor

# teclado={
#     "marca":"klipextreme",
#     "cantTeclas":158,
#     "color":"negro",
#     "inalambrico":True
# }
# print(teclado)

# # Le puedo ir agregando claves
# teclado["tienePadNumerico"]=True
# teclado["cantTeclas"]=58

# print(teclado)

# -------------------------------------------

# alumno={}
# # Si la clave no existe la agrega, y si la clave existe la modifica
# alumno["nombre"]="Juan"
# alumno["edad"]=32
# alumno["nacionalidad"]="Argentina"
# alumno["materias"]=["Matematica","Lengua","Ciencias Naturales"]

# print(alumno)

# print(alumno["nacionalidad"])

# # Obtengo la cantidad de elementos de alumno
# print(len(alumno))

# print(alumno.get("materias"))
# print(alumno.get("nacionalidad"))


# ------------------------------------------------

enfermera={
    "nombre":"Ana",
    "especialidad":"Hemoterapia",
}

enfermera1={
    "especialidad":"Hemoterapia",
    "nombre":"Ana"
}

# Se pueden comparar ""=="", ejemplo. Misma clave-valor y que sean iguales
if enfermera==enfermera1:
    print("Son iguales")
else:
    print("No son iguales")


# ------------------------------------------------
#Metodos de diccionarios 
# ------------------------------------------------

#Get (clave) Devolver el valor que tiene una clave 

#Valor por defecto, si es que no existe

# print(enfermera.get("peso","-"))

# ----

#Recorrer un diccionario 

# #items 

# (desempaquetado)
for key,value in enfermera.items():
     print(f"Clave: {key} y Valor: {value}") #Esto es formatString

#Obtener solo las claves 

for key in enfermera.keys():
    print(key)

#Obtener solo los valores

for key in enfermera.values():
    print(key)

# #Eliminar elemento de un diccionario 

# print(enfermera)

# if "edad" in enfermera:
#     del enfermera["edad"]
# else:
#     print("No existe tal clave")

# print(enfermera)

# ***********
# jugares: es una lista de diccionarios
# ***********

# clubesFutbol=[
#     {"nombre":"Boca Juniors",
#      "barrio": "La Boca",
#      "cantHinchas":50000000,
#      "jugadores":[
#          {
#              "nombre":"Cavani",
#              "numero":10
#          }
#      ]
#      },
# {"nombre":"River Plate",
#      "barrio": "Nuñez",
#      "cantHinchas":40000000
#      },
# {"nombre":"Chacarita",
#      "barrio": "Chacarita",
#      "cantHinchas":30000000
#      }
# ]

# print(clubesFutbol)

# clubesFutbol.append({"nombre":"Velez","barrio":"Liniers","cantHinchas":10})
# print(clubesFutbol)

# print(clubesFutbol[3]["cantHinchas"])

# for clubcito in clubesFutbol:
#     print(f"Nombre {clubcito["nombre"]} Barrio {clubcito["barrio"]} Cantidad de Hinchas {clubcito["cantHinchas"]}")


# ---------------------------------------------------
# Buscar un valor especifico dentro de un diccionario
# --------------------------------------------------
# america={
#     "nombre":"America",
#     "cantHabitantes":14000,
#     "fundador":{
#         "nombre": "Gemesio",
#         "anioFundacion":1900
#     }
# }

# print(f"Nombre del fundador de America: {america["fundador"]["nombre"]} ")


dict() #Lo que le pasamos por parametro lo convierte a diccionario