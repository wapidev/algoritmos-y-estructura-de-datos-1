import re 


# EJEMPLO 1 - begin

# palabras=["carrito","carton","collar","pepe cartel"]

# pattern='car+'

# for palabra in palabras:
#     if re.match(pattern,palabra):
#         print(palabra," coincide ")
#     else:
#         print(palabra, "no coincide")

# EJEMPLO 1 - end

# --------------------------------------------------

# EJEMPLO 2 - begin

#Que empiece con una letra que puede ser cualquiera en mayuscula o minuscula y 
#luego continue con tres numeros entre 1 y 3

# cadenas=['A123','D555','P999','J258','1Z111','L259']

# patron='[A-Za-z][111-888]' #empieze con cualquier letra, 3 veces, rango de 

# for cadena in cadenas:
#     if re.search(patron,cadena):
#         print(cadena," coincide ")
#     else:
#         print(cadena, " no coincide")

# *Diferencia entre MATCH y SEARCH*. 
# MATCH Evalua solo al inicio de la cadena
# SEARCH Evalua a lo largo de toda la cadena


# EJEMPLO 2 - end

# --------------------------------------------------


# EJEMPLO 3 - begin

palabrita="L888"
patron='[A-Za-z][111-888]'

objetoMatch= re.search(patron,palabrita,re.IGNORECASE) ##re.IGNORECASE es para ignorar mayuscula y minuscula
if(objetoMatch):
    print(objetoMatch.group()) #donde encuentra el matc
    print(objetoMatch.start()) #en que posicion inicia el match
    print(objetoMatch.end()) #en que posición termina el match


# Ejemplo de caracteres varias veces
# A-Z 2 veces, 0-9 3 veces, A-z 2 veces
# patentes='[A-Z]{2}[0-9]{3}[A-Z]{2}'

# EJEMPLO 3 - end

