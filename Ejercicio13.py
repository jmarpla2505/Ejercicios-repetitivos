#Una empresa tiene el registro de las horas que trabaja diariamente un empleado
#durante la semana (seis días) y requiere determinar el total de éstas, así como el
#sueldo que recibirá por las horas trabajadas.
horas = 0
vHoras = []
horasemana = 0
sueldo = 0
for i in range(1,7):
    horas=int(input("Horas trabajadas en este día:"))
    vHoras.append(horas)
    horasemana = horas + horasemana

print("En toda la semana ha trabajado", horasemana)
sueldo = int(input("Dime cuanto dinero gana por cada hora trabajada:"))
print("Habrá ganado", sueldo*horasemana)


