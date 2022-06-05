import random

piedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tijera = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

elementos = [piedra, papel, tijera]

print("Cual es tu eleccion? Pulsa 0 para Piedra, 1 para papel o 2 para Tijeras.")

player_one = int(input("Cual es tu eleccion?????: "))

print(elementos[player_one])

computer_number = random.randint(0, (len(elementos) -1)) 

print("La computadora elige: ")

print(elementos[computer_number])

if elementos[player_one] == elementos[0] and elementos[computer_number] == elementos[1]:
    print("Perdiste")
elif elementos[player_one] == elementos[1] and elementos[computer_number] == elementos[2]:    
    print("Perdiste")
elif elementos[player_one] == elementos[2] and elementos[computer_number] == elementos[0]:    
    print("Perdiste")
elif elementos[player_one] == elementos[computer_number]:
    print("Empate")
else:
    print("Ganaste!!")        
