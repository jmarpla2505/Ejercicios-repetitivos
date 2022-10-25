#Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’
#en caso contrario, el programa termina cuando se introduce un espacio.

caracter = ""

while caracter!=" ":
    caracter = input("Dime un caracter:")
    if caracter=="a" or "A" or "e" or "E" or "i" or "I" or "o" or "O" or "u" or "U":
        print("Es una vocal")
    else:
        print("No es vocal")
    
print("EL programa ha terminado")