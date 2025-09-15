# Ejercicio 1.
# Desarrolle un programa que almacene datos de canciones en formato MP3: 
# Artista, Título, Duración (en segundos), 
# Tamaño del fichero (en KB). 
# Un programa debe pedir los datos de una canción al usuario y después 
# mostrarlos en pantalla. 
# Debe interrumpirse la carga cuando el artista ingresado sea vacío.

# Programa que almacena datos de canciones en formato MP3

canciones = []

artista = input("Ingrese el nombre del artista (deje vacío para terminar): ")

while artista!="":
    cancion={}
    cancion["artista"] = artista
    cancion["titulo"] = input("Ingrese el título de la canción: ")
    cancion["duracion"] = int(input("Ingrese la duración de la canción (en segundos): "))
    cancion["tamaño"] = int(input("ingrese el tamaño de la cancion (en kb)"))

    canciones.append(cancion)

    artista = input("Ingrese el nombre del artista (deje vacío para terminar): ")

print("canciones: ", canciones)


