python 

import random 

print (" instrucciones: \n Tijera corta a papel \n Papel tapa a piedra \n Piedra aplasta a lagarto \n Lagarto envenena a Spock \n Spock rompe a tijera \n Tijera decapita a lagarto \n Lagarto devora a papel \n Papel desautoriza a Spock \n Spock vaporiza a piedra \n Piedra aplasta a tijera")

user=input("elige entre piedra, papel, tijera, lagarto, spock " + " ").lower()

options=["piedra""", "papel", "tijera", "lagarto", "spock"]
computer=options[random.randint(0,4)]
print(f"la computadora eligio {computer}")
if (user=="tijera"):
  if computer=="papel":
   print("tijera corta papel, ganaste")
  elif computer=="piedra":
    print("piedra aplasta tijera, perdiste")
  elif computer=="tijera":
    print("empate")
  elif computer=="lagarto":
    print("tijera decapita lagarto, ganaste")
  elif computer=="spock":
    print("spock rompe tijera, perdiste")

elif (user=="piedra"):
  if computer=="papel":
    print("papel tapa piedra, ganaste")
  elif computer=="piedra":
    print("empate")
  elif computer=="tijera":
    print("piedra rompe tijera, ganaste")
  elif computer=="lagarto":
    print("piedra aplasta lagarto, ganaste")
  elif computer=="spock":
    print("spock vaporiza piedra, perdiste")
    
elif (user=="papel"):
  if computer=="papel":
    print("empate")
  elif computer=="piedra":
    print("papel tapa piedra, ganaste")  
  elif computer=="tijera":
    print("tijera corta papel, perdiste")
  elif computer=="lagarto":
    print("lagarto devora papel, perdiste")
  elif computer=="spock":
     print("papel desautoriza spock, ganaste")
    
elif (user=="lagarto"):
  if computer=="papel":
    print("lagarto devora papel, ganaste")
  elif computer=="piedra":
    print("piedra aplasta lagarto, perdiste")
  elif computer=="tijera":
    print("tijera decapita lagarto, perdiste")
  elif computer=="lagarto":
    print("empate")
  elif computer=="spock":
    print("lagarto envenena spock, ganaste")
    
elif (user=="spock"):
  if computer=="papel":
    print("papel dasautoriza spock, perdiste")
  elif computer=="piedra":
    print("spock vaporiza piedra, ganaste")
  elif computer=="tijera":
    print("tijera decapita spock, perdiste")
  elif computer=="lagarto":
    print("lagarto envenena spock, perdiste")
  elif computer=="spock":
    print("empate")
    
else:
  print("no es una opcion valida")
  
print("gracias por jugar")
