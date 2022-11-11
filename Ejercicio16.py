#Una empresa les paga a sus empleados con base en las horas trabajadas en la
#semana. Realice un algoritmo para determinar el sueldo semanal de N
#trabajadores y, además, calcule cuánto pagó la empresa por los N empleados.
horas = 0
numerotrabajadores = 0

numerotrabajadores = int(input("Dime cuántos trabajadores tiene la empresa:"))
sueldohora = 0
sueldohora = int(input("Dime cuanto paga la empresa por hora:"))
vHoras = []
horastotales = 0

for i in range(numerotrabajadores):
    horas = int(input("Dime cuantas horas ha trabajado el trabajador:"))
    vHoras.append(horas)
    print("Este trabajador ha cobrado", horas*sueldohora)
    horastotales = horas + horastotales

print("La empresa pagó un sueldo total a los empleados de", horastotales*sueldohora)



