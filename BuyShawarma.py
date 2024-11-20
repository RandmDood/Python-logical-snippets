size = (input("Welcome to Davy's Shawarma\nWould you like to order a small, medium, or large shawarma? "))
hotdogs = (input("Would you like hotdogs?  "))
sauce = (input("Would you like extra sauce?  "))
bill = 0
if size == "small":
	bill += 1500
elif hotdogs == "yes":
		bill += 200
if sauce == "yes":
	print(f"Your bill is #{bill + 300}")
bill = 0
if size == "medium":
	bill += 2000
elif hotdogs == "yes":
		bill += 300
if sauce == "yes":
	print(f"Your bill is #{bill + 300}")
bill = 0
if size == "large":
	bill += 3000
elif hotdogs == "yes":
		bill += 300
if sauce == "yes":
			print(f"Your bill is #{bill + 300}")

	