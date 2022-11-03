#Escribe un programa que pida el limite inferior y superior de un intervalo. Si el
#límite inferior es mayor que el superior lo tiene que volver a pedir.
#A continuación se van introduciendo números hasta que introduzcamos el 0.
#Cuando termine el programa dará las siguientes informaciones:
# La suma de los números que están dentro del intervalo (intervalo abierto).
# Cuantos números están fuera del intervalo.
# He informa si hemos introducido algún número igual a los límites del intervalo.

lista = []
sumaintervalo = []
fueraintervalo = []
num = 1
igualintervalo = []
lista.append(sumaintervalo)
lista.append(fueraintervalo)
lista.append(igualintervalo)
suma= 0
try:
    limiteinferior = int(input("Dime el límite inferior:"))
    limitesuperior = int(input("Dime el límite superior:"))
    if limiteinferior<limitesuperior:
         while num!= 0:
            num = int(input("Dime un número:"))
            if limiteinferior<num<limitesuperior:
                sumaintervalo.append(num)
                
            elif num>limitesuperior or num<limiteinferior:
                fueraintervalo.append(num)
                
            else:
                igualintervalo.append(num)
                


    else:
        print("El límite inferior tiene que ser menor que el límite superior")
    limiteinferior = int(input("Dime el límite inferior:"))
    limitesuperior = int(input("Dime el límite superior:"))
    while num!= 0:
            num = int(input("Dime un número:"))
            if limiteinferior<num<limitesuperior:
                sumaintervalo.append(num)
                
            elif num>limitesuperior or num<limiteinferior:
                fueraintervalo.append(num)
                
            else:
                igualintervalo.append(num)
except:
    print("Tienes que introducir números")


for lista in sumaintervalo:
    suma += lista





print("La suma de los número del intervalo es", suma)
print("Números que están fuera del intervalo:", fueraintervalo)
print("Números introducidos iguales a los intervalos:", igualintervalo)




