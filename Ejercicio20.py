#Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad
#de números primos que queremos mostrar.


Vnum=[]
i=2
numerodeprim=int(input("Dime cuántos números primos quieres que se muestren:"))
contador = numerodeprim

def numero_primo(numero):
    num_primo=0
    for i in range (2,numero):
        if numero%i==0:
            num_primo+=1
    if num_primo>=1:
        return False
    else:
        return True
    

while contador>0:
    if numero_primo(i)==True:
        Vnum.append(i)
        contador-=1
    i+=1
print(Vnum)
