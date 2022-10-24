#Crea una aplicación que pida un número y calcule su factorial (El factorial de un
#número es el producto de todos los enteros entre 1 y el propio número y se
#representa por el número seguido de un signo de exclamación. Por ejemplo 5! =
#1x2x3x4x5=120)

numero = 0
numero = int(input("Dime un número:\n"))
resultado = 1

for num in range(1,numero+1):
  resultado = resultado*num
  
print("El factorial de", numero, "es",resultado)
    