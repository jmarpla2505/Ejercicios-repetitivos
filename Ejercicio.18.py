#Hacer un programa que muestre un cronometro, indicando las horas, minutos y 
#segundos.

import os
import time

for hora in range(24):
    for minuto in range(60):
        for segundo in range(60):
            os.system('cls')
            print(hora,":",minuto,":",segundo)
            time.sleep(1)
