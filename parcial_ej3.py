from random import randint

def generador_matriz_triangular(numero):
    #validar variable numero para generar matriz
    lista_matriz = []
    if type(numero) != int:
        return lista_matriz
    elif numero < 2:
        return lista_matriz
    else:
        #n listas de n elementos, incrementando la cantidad de ceros
        #a partir del primer indice de la segunda lista,
        #llenando el resto aleatoriamente
        for i in range(numero):
            linea = ([0] * i + [randint(1, 9)] * (numero - i))
            lista_matriz.insert((i),linea)
        return lista_matriz


#print (generador_matriz_triangular(1))


def ejercicio3(var1):
    return generador_matriz_triangular(var1)


print(ejercicio3(-1)) # []
print(ejercicio3(0)) # []
print(ejercicio3(1)) # []
print(ejercicio3(2)) # [[x,x],[0,x]]
print(ejercicio3(3)) # [[x,x,x],[0,x,x],[0,0,x]]
print(ejercicio3(4)) # [[x,x,x,x],[0,x,x,x],[0,0,x,x],[0,0,0,x]]
print(ejercicio3("4")) #[]
print(ejercicio3("PEPE")) #[]
print(ejercicio3(2.5)) #[]
