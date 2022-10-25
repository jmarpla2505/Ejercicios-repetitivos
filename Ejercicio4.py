#Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de
#números a introducir). El programa debe informar de cuantos números
#introducidos son mayores que 0, menores que 0 e iguales a 0.

num = 0
numerodepreguntas = 0
mayorquecero = 0
igualquecero = 0
menorquecero = 0

numerodepreguntas = int(input("Cúantos numeros quieres introducir:"))

for numero in range(numerodepreguntas):
    num = int(input("Dime un número:"))

    if num>0:
        mayorquecero += 1
    elif num == 0:
        igualquecero += 1
    else:
        menorquecero += 1

print(mayorquecero, "numeros son mayores que cero", igualquecero, ", numeros son iguales que cero", menorquecero, ", numeros son menores que cero")