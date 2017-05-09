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



def ejercicio4(var1):
    return torneo_liga(var1)

campeonato = []
print(ejercicio4(campeonato)) # ""

campeonato = [("a",1,"b",0)]
print(ejercicio4(campeonato)) # a

campeonato = [("a",1,"b",0),("a",1,"c",2),("c",3,"b",0)]
print(ejercicio4(campeonato)) # c

campeonato = [("a",1,"b",1),("a",1,"c",1),("c",1,"b",1)]
print(ejercicio4(campeonato)) # a  b  c (cualquiera de las 3)

campeonato = [("a",1,"b",-2),("a",1,"c",1),("c",1,"b",1),("d",1,"a",9)]
print(ejercicio4(campeonato)) # a