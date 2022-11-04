#Escribe un programa que diga si un número introducido por teclado es o no
#primo. Un número primo es aquel que sólo es divisible entre él mismo y la
#unidad. Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si
#es divisible por algún otro número.

num = 0
num = int(input("Dime un número:"))
contador = 0
for i in range (2,num):
    if num%i == 0:
        contador += 1

if contador >= 1:
    print(num,"No es primo")
else:
    print(num,"Es primo")

