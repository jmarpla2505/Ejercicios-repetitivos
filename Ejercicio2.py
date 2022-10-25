#Crea una aplicación que permita adivinar un número. La aplicación genera un
#número aleatorio del 1 al 100. A continuación va pidiendo números y va
#respondiendo si el número a adivinar es mayor o menor que el introducido,a
#demás de los intentos que te quedan (tienes 10 intentos para acertarlo). El
#programa termina cuando se acierta el número (además te dice en cuantos
#intentos lo has acertado), si se llega al limite de intentos te muestra el número
#que había generado.


import random

numsecreto = random.randint(1,101)
numero1= 0
contador=0
numero1 = int(input("Dime un número:"))
while numero1!=numsecreto and contador<10:
    if numero1>numsecreto:
        print("El número secreto es menor")
    else:
        print("El número secreto es mayor")
    contador +=1
    numero1 = int(input("Dime un número:"))
    print("Te quedan", 9-contador, "intentos")

if numero1==numsecreto:
    print("Enhorabuena, lo has adivinado en", contador, "intentos")
else:
    print("El número generado era", numsecreto)