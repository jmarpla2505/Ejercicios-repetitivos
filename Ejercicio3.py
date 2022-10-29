#Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la
#suma y la media de todos los números introducidos.

numero = (int)(input("Dime un número:"))
suma = 0
contador = 0
while numero != 0:
    suma = suma + numero
    contador = contador + 1
    numero = (int)(input("Dime otro número o pulsa 0 para salir:\n"))

print("La suma de los números es:", suma)
print("La media de los números es:", suma/contador)