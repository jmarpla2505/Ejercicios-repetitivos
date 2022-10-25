#Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la
#suma y la media de todos los números introducidos.

num=1
media = 0
vDatos = []
contador=0
while num!=0:
    num = int(input("Dime un número:"))
    if (num!=0):
        vDatos.append(num)
    contador += 1

for numero in vDatos:
    print("La media es", (numero*contador)/contador)
    print("La suma es", numero*(contador-1))