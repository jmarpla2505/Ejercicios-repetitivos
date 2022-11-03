#Escribe un programa que dados dos números, uno real (base) y un entero
#positivo (exponente), saque por pantalla el resultado de la potencia. No se puede
#utilizar el operador de potencia.
base = 0
exponente = 0
base = int(input("Dime un número real como base:"))
exponente = int(input("Dime un número entero positivo como exponente:"))

potencia=1
for num in range(exponente):
     potencia=potencia*base

print("La potencia es"%potencia)