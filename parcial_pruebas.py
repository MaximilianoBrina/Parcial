from parcial_modulo import *

print ("Ejercicio 1")
def ejercicio1(var1,var2):
    return divisores(var1,var2)


print(ejercicio1("",[1,2,3])) # []
print(ejercicio1(-1,[1,2,3])) # []
print(ejercicio1(0,[1,2,3])) # []
print(ejercicio1(0,[])) # []
print(ejercicio1(1,[1,2])) # [1]
print(ejercicio1(2,[1,-2])) # [1,-2]
print(ejercicio1(8,[1,7,2,-4,6,9])) # [1,2,-4]
print(ejercicio1(331,[1,2,3,7,147,331,518])) # [1,331]

print ("")
print ("Ejercicio 2")
def ejercicio2(var1,var2):
    return validar_extension(var1,var2)


print(ejercicio2('/home/user/listado.txt',['mp3','wav','mpeg'])) # False
print(ejercicio2('/home/user/listado.txt',['mp3','wav','mpeg','txt'])) # True
print(ejercicio2('/home/user/listado.txt',['mp3','wav','mpeg','TXT'])) # True
print(ejercicio2('/home/user/listado.tXt',['mp3','wav','mpeg','TXT'])) # True
print(ejercicio2('/home/user/listado.txt',['txt'])) # True
print(ejercicio2('/home/user/listado',['mp3','wav','mpeg','txt'])) # False
print(ejercicio2('/home/user/listado',[])) # False
print(ejercicio2('',[])) # False

print("")
print ("Ejercicio 3")
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

print("")
print ("Ejercicio 4")
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