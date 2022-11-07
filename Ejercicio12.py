#Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, si
#al final de cada mes deposita cantidades variables de dinero; además, se quiere
#saber cuánto lleva ahorrado cada mes.

vAhorros = []
suma = 0
ahorroaño = 0
for i in range(1,13):
    num = int(input("Dime cuanto ha ahorrado este mes:"))
    vAhorros.append(num)
    ahorroaño = num + ahorroaño

print("En todo el año ha ahorrado", ahorroaño)
