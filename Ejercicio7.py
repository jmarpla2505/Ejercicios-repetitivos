#Realizar una algoritmo que muestre la tabla de multiplicar de un número
#introducido por teclado.

numero = 0
numero = int(input("Dime un número:"))
contador = 0

while contador<10:
    contador += 1
    print(numero, "*", contador, "=", numero*contador)

