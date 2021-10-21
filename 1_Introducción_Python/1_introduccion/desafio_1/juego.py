import random
import sys

seleccion = (sys.argv[1])

if seleccion == "papel":
    juego1=1
    print("usuario juega papel")
elif seleccion == "piedra":
    juego1=2
    print("usuario juega piedra")
elif seleccion == "tijera":
    juego1=3
    print("usuario juega tijera")
else:
    juego1=""

juego2=random.randint(1,3)
if juego2 == 1:
    print("computador juega papel")
elif juego2 == 2:
    print("computador juega piedra")
elif juego2 == 3:
    print("computador juega tijera")

if juego1 == juego2: 
    print("empate")
elif juego1 == 1 and juego2 == 2: 
    print("usuario gana")
elif juego1 == 1 and juego2 == 3: 
    print("computador gana")
elif juego1 == 2 and juego2 == 1: 
    print("computador gana")
elif juego1 == 2 and juego2 == 3: 
    print("usuario gana")
elif juego1 == 3 and juego2 == 1: 
    print("usuario gana")
elif juego1 == 3 and juego2 == 2: 
    print("computador gana")
else:
    print("juegue denuevo")