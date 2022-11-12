#Realizar un ejemplo de menú, donde podemos escoger las distintas opciones 
#hasta que seleccionamos la opción de “Salir”.

menuprincipal = int(input("Menú principal:\n 1-Opción 1\n 2-Opción 2\n 3-Opción 3\n 4-Opción 4\n 5-Salir\n"))

while menuprincipal!=5:

    if menuprincipal==1:
        print("Has seleccionado la opción 1")
    elif menuprincipal==2:
        print("Has seleccionado la opción 2")
    elif menuprincipal==3:
        print("Has seleccionado la opción 3")
    elif menuprincipal==4:
        print("Has seleccionado la opción 4")
    else:
        print("Introduce una de las 5 opciones")
        
    menuprincipal = int(input("Menú principal:\n 1-Opción 1\n 2-Opción 2\n 3-Opción 3\n 4-Opción 4\n 5-Salir\n"))

print("Has salido del menú")
