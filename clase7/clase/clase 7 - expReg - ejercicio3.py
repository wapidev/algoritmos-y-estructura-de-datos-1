"""
Pedirle una cadena al usuario y validar si la misma comienza con una letra mayuscula. 
Informar verdadero o falso.
"""

import re 

pattern='^[A-Z]'

# ^ se usa para validar si comienza
# si se usa match, no es necesario usar ^

fraseIngresada=input("Ingresa una frase")

if re.match(pattern,fraseIngresada): #con el match es suficiente porque comienza a evaluar desde el principio
    print("Verdadero")

