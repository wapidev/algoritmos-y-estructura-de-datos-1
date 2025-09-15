# Programa que lee datos de tres personas y muestra la más joven

personas = {}

for i in range(1, 4):
    print(f"\nIngrese los datos de la persona {i}:")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    genero = input("Género: ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")

    personas[nombre] = {
        "edad": edad,
        "genero": genero,
        "direccion": direccion,
        "telefono": telefono
    }

print("\n--- Datos de las personas ---")
for nombre, datos in personas.items():
    print(f"\nNombre: {nombre}")
    print(f"Edad: {datos['edad']}")
    print(f"Género: {datos['genero']}")
    print(f"Dirección: {datos['direccion']}")
    print(f"Teléfono: {datos['telefono']}")

# Ordenamos por edad (menor primero)
personas_ordenadas = sorted(personas.items(), key=lambda x: x[1]["edad"])
mas_joven = personas_ordenadas[0]  # el primero es el menor

print("\nLa persona más joven es:", mas_joven[0], "con", mas_joven[1]["edad"], "años")