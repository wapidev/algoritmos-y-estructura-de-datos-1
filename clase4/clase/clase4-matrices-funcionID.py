numeroA=11
numeroB=33
nombre="Juan"
numeroC=11
nombrecito="Juan"

print(id(numeroA))
print(id(numeroB))
print(id(nombre))
print(id(numeroC))


lista=[1,2,3,4]
lista2=lista
lista2.append(5)

if lista is lista2:
    print("Son el mismo identificador")
else:
    print("No son el mismo identificador")

print(lista)  #1,2,3,4
print(lista2) #1,2,3,4,5

print(id(nombre))
print(id(nombrecito))

print("Nombre y nombrecito tienen el mismo identificador?? ", nombre is nombrecito)


