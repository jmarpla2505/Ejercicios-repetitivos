#Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó
#10 €, el segundo 20 €, el tercero 40 € y así sucesivamente. Realizar un algoritmo
#para determinar cuánto debe pagar mensualmente y el total de
#lo que pagó después de los 20 meses.
pagototal = 0
primerpago = 10
pagopormes = 0
for i in range(1,21):
   print("En el mes", i, "pagó", primerpago)
   pagototal = pagototal + primerpago
   primerpago = primerpago*2 

print("A los 20 meses pago", pagototal)