"""
Pedirle al usuario que ingrese una cadena y vamos a buscar todas las 
letras mayusculas en esa cadena y las vamos a imprimir. 
"""

import re 

fraseUsuario= input("Ingrese una frase")

patron='[A-Z]'

mayusculas= re.findall(patron,fraseUsuario)

for mayusculita in mayusculas:
    print(mayusculita)