print("Welcome to the treasure island.")
print("Your mision is to find the treasure")

move = input("Move left or rigth?? <Left, Right>").lower()

if move == "left":

	action = input("Do you wanna swim or wait?? <Swim, Wait>").lower()

	if action == "wait":

		door = input("Wich door ?? <Red, Blue, Yellow>")

		if door == "yellow":

			print("You Win!!")

		else:

			print("Game Over")	
	
	else:
	
		print("Game Over")	

else:
	print("Game Over")