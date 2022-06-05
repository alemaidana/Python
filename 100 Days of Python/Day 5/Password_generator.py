import random

print("Welcome to the PyPassword Generator!")


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

n_letters = int(input("Hoy many letters would you like in your password?"))
n_symbols = int(input("How many symbols would you like?"))
n_numbers = int(input("How many numbers would you like?"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""

for i in range(0, n_letters):

	aleatorio = random.randint(0, len(letters) - 1)
	password += letters[aleatorio]


for i in range(0, n_symbols):

	aleatorio = random.randint(0, len(symbols) - 1 )
	password += symbols[aleatorio]



for i in range(0, n_numbers):

	aleatorio = random.randint(0, len(numbers) - 1)
	password += numbers[aleatorio]


print("Here is your password:", password)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

hard_pass = ""

hard_num = n_letters + n_numbers + n_symbols
final_list = numbers + letters + symbols

for j in range(0, hard_num):
	aleatorio_hard = random.randint(0, len(final_list) - 1)	
	hard_pass += final_list[aleatorio_hard]


print("Here is your hard password:", hard_pass)
