#If the bill was 150.00 split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12

#print(round(150 * 1.12, 2))

print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

total = "{:.2f}".format((bill * ((tip / 100) + 1)) / people)

print(f"Each people should pay: ${total}")

