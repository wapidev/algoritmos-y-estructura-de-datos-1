"""1.	Desarrolle un programa que almacene datos de canciones en formato MP3: 
Artista, Título, Duración (en segundos), Tamaño del fichero (en KB). 
Un programa debe pedir los datos de una canción al usuario y después mostrarlos en pantalla. 
Debe interrumpirse la carga cuando el artista ingresado sea vacío."""

canciones=[] #Es una lista de diccionarios

artista=input("Ingrese el nombre del artista que canta la cancion: ")

while artista!="":
    cancion={}

    cancion["artista"]= artista
    cancion["titulo"]= input("Ingrese el titulo de la canción: ")
    cancion["duracion"]=int(input("Ingrese la duracion de la cancion en minutos: "))
    cancion["kb"] = int(input("Ingrese el tamaño en KB del archivo: "))

    canciones.append(cancion)

    artista=input("Ingrese el nombre del artista que canta la canción: ")


for cancion in canciones:
    print(f"Artista {cancion['artista']}")    
    print(f"Titulo: {cancion['titulo']}")    
    print(f"Duración: {cancion['duracion']}")    
    print(f"Tamaño: {cancion['kb']}")    
    print("------------------------------------------")
    




