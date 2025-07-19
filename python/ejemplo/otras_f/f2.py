def mayor(lista):
    mayor = lista[0] 
    for i in range(len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
    return mayor
#TODO: def menor