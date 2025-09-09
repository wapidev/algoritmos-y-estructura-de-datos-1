def sumarMatrices(matriz1,matriz2):
    filas = len(matriz1)
    columnas = len(matriz1[0])

    matrizResultado=[]

    for fila in range(filas):
        filaSuma=[]
        for columna in range(columnas):
            elementoSuma = matriz1[fila][columna] + matriz2[fila][columna]
            filaSuma.append(elementoSuma)
        matrizResultado.append(filaSuma)
    return matrizResultado



matriz1=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matriz2=[
    [9,8,7],
    [6,5,4],
    [3,2,1]
]


print(sumarMatrices(matriz1,matriz2))
