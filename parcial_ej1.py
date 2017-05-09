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