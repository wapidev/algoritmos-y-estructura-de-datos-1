"""Validar si una cadena es una patente y cumpla con alguna de las 2 formas
AA000AA
AAA000
"""
import re 

# patronPatenteModerna='[A][A-H][0-9]{3}[A-Z]{2})'
# patentesModernas=['AF512SP','AJ512SP','LJH258','KIK147','PEPE147']

# for patenteModerna in patentesModernas:
#     if re.match(patronPatenteModerna,patenteModerna):
#         print(patenteModerna," - Dió match")
#     else:
#         print(patenteModerna,"- NO dió match")


patronPatenteVieja='[A-Z]{3}[0-9]{3}'
patentesVieja=['LJH258','KIK147','PEPE145']

for patenteVieja in patentesVieja:
    if re.match(patronPatenteVieja,patenteVieja):
        print(patenteVieja," - Dió match")
    else:
        print(patenteVieja,"- NO dió match")

# patronPatente='([A][A-H][0-9]{3}[A-Z]{2})|([A-Z]{3}[0-9]{3})'
# Para agrupar patrones se pone ()|()