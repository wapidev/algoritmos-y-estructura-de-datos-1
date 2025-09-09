matriz = [
    ['a','b','c','d'],
    [1,2,3,4],
    [5,6,7,8]
]

print(matriz[0][3])
print(matriz[1][0])

for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        print(matriz[fila][columna])



