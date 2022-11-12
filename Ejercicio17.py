#Una empresa les paga a sus empleados con base en las horas trabajadas en la 
#semana. Para esto, se registran los días que trabajó y las horas de cada día. 
#Realice un algoritmo para determinar el sueldo semanal de N trabajadores y 
#además calcule cuánto pagó la empresa por los N empleados.

horas = 0
numerotrabajadores = 0

numerotrabajadores = int(input("Dime cuántos trabajadores tiene la empresa:"))
sueldohora = 0
sueldohora = int(input("Dime cuanto paga la empresa por hora:"))
horastotales = 0
diastotales = 0
vHoras = []
suma = 0
lista = []

for i in range(numerotrabajadores):
    dias = int(input("Dime cuantos días ha trabajado:"))
    for i in range(dias):
        horas = int(input("Dime cuantas horas ha trabajado en ese día:"))
        horastotales = horas + horastotales
        vHoras.append(horas)
        lista.append(vHoras)
    print("Este trabajador ha cobrado", horastotales*sueldohora)
    horastotales = 0
    horas = 0

suma = sum(vHoras)
print("La empresa pagó un sueldo total a los empleados de", suma*sueldohora)