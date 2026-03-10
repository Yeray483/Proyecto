# Yeray

from random import randrange

def LanzarDado():
    dado1=randrange(1,7)
    print("Ha salido ",dado1)
    dado2=randrange(1,7)
    print("Ha salido ",dado2)
    suma=dado1+dado2
    return suma

def solicitar_apuesta(credito):
    apuesta=int(input("Cuánto quieres apostar?"))
    return(apuesta)

credito=100
while: 
   total1=LanzarDado()
   print(total1)
    
