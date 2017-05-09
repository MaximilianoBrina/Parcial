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


#validar_extension("pepe/pepe/pepe",["txt","mp3","mpeg","jpg"])

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