def determinarCapicua(lista):
    izquierda=0
    derecha=len(lista)-1

    while(izquierda<derecha):
        if lista[izquierda]!= lista[derecha]:
            return False
        izquierda+=1
        derecha-=1
    
    return True



