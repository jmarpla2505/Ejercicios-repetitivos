#Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, si
#al final de cada mes deposita cantidades variables de dinero; además, se quiere
#saber cuánto lleva ahorrado cada mes.

vAhorros = []
suma = 0
for n in range(1,13):
    num = int(input("Dime cuanto ha ahorrado en el mes", n))
    vAhorros.append(num)

print("En todo el año ha ahorrado")
for vAhorros in num:
    suma += vAhorros