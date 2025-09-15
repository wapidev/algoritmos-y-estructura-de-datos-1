"""
+ - 1 o mas veces el elemento antecesor 
* - 0 o mas veces el elemento antecesor 
? - 0 o 1 vez el elemento antecesor

Vamos a buscar todas las ocurrencias de numeros en una cadena. 
Devolver todos los numeros  
l14kil5

"""
import re

cadena = 'epe1lola5luis88p8mirna'

resultadosNumeros= re.findall('[0-9]+',cadena)

print(resultadosNumeros)
