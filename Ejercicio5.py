#Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’
#en caso contrario, el programa termina cuando se introduce un espacio.

caracter = ""

while caracter!=" ":
    caracter = input("Dime un caracter:").upper()
    if (caracter=="a" or caracter=="e" or caracter=="i" or caracter=="o" or caracter=="u"):
        print("Es una vocal")
    else:
        print("No es vocal")
    
print("EL programa ha terminado")