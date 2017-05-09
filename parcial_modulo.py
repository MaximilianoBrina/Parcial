#ej1
def divisores(n,lista):
    if type(n) == int and n > 0:
        listaDivisores = []
        for i in lista:
            resto = n % i
            if resto == 0:
                listaDivisores.append(i)
        return listaDivisores
    else:
        listadivisores = []
        return listadivisores


#ej2
def normalizar_lista(lista):
    for i in range(len(lista)):
        lista[i] = lista[i].lower()
    return lista

def validar_extension(ruta, extensiones):
    # normalizar ruta y extensiones
    ruta = ruta.lower()
    extensiones = (normalizar_lista(extensiones))

    # obtener extension del archivo si existe
    if "." not in ruta:
        return False
    else:
        exten = ruta.index(".")
        punto = ruta.index(".")
        exten = ruta[(int(punto) + 1):(int(punto) + 5)]  # concibe la posibilidad de extensiones de 2 (.py), 3 (.mp3) o 4 (.mpeg) caracteres

        # contrastar extension del archivo en la ruta con la lista de extensiones validas
        if exten in extensiones:
            return True
    return False

#ej3
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

#ej4
def ganador_torneo(lista): #devuelve el ganador del torneo
    goles = list(lista.values())
    equipos = list(lista.keys())
    return equipos[goles.index(max(goles))]

def torneo_liga(partidos): #procesa resultados de los partidos del torneo
    torneo = {}
    ganador = ""
    perdedor = ""

    #cheq. si la lista esta vacia
    if len(partidos) == 0:
        return ""

    #procesar las tuplas
    for i in range (len(partidos)):
        #empate
        if partidos[i][1] == partidos[i][3]:
            torneo[partidos[i][0]] = 1
            torneo[partidos[i][2]] = 1
        #definir ganadores-perdedores
        else:
            if (max(partidos[i][1],partidos[i][3])) == partidos[i][3]:
                ganador = (partidos[i][2])
                perdedor = (partidos[i][0])
            else:
                ganador = (partidos[i][0])
                perdedor = (partidos[i][2])

            if ganador in torneo:
                torneo[ganador]=int(torneo[ganador])+2
            else:
                torneo[ganador] = 2

            if perdedor in torneo:
                torneo[perdedor]=int(torneo[perdedor])+0
            else:
                torneo[perdedor] = 0
    #procesar resultados obtenidos y definir ganador
    return ganador_torneo(torneo)