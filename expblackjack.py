import random
all = {"ace": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "king": 10, "queen": 10, "jack": 10}
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
repres = ["ace",2,3,4,5,6,7,8,9,10,"king","queen","jack"]

random.shuffle(repres)

stake = ""
player = []
dealer = []
n = 0
x = []
y = []

new_arrangement = []
for rep in repres:
	new_arrangement.append(rep)

def give():
	global n
	global x
	global y
	player.append(new_arrangement[n])
	x.append(all[str(new_arrangement[n])])
	
	dealer.append(new_arrangement[-(n+1)])
	y.append(all[str(new_arrangement[-(n + 1)])])
	
	n += 1
n = 0
		
def give_only_player():
	global n
	global x
	player.append(new_arrangement[n])
	x.append(all[str(new_arrangement[n])])
	print(f"your cards are: {player}")
	n += 1
n = 0

stake = ""
player = []
dealer = []
n = 0
x = []
y = []		
def game():
	global stake
	random.shuffle(repres)
	new_arrangement = []
	for rep in repres:
		new_arrangement.append(rep)
	print(new_arrangement)
	give()
	give()
	print(f"Your cards are: {player}")
	print(f"The dealer has 2 cards. One of which is {dealer[0]}")
	while stake != "s":	
		stake = input("enter S to stand, enter any key to pick another card").lower()
		if stake != "s":
			give_only_player()
		total_x = sum(x)
		if total_x > 21:
			for paper in player:
				if paper == "ace":
					total_x  -= 10
	
	if total_x == sum(y):
		print("Draw")			
	elif total_x > sum(y) and total_x <= 21:
		print(f"Congregations! You win.\nYour cards are: {player}\nThe dealer's cards are {dealer}")
	else:
		print(f"You lost.\nYour cards are: {player}\nThe dealer's cards are {dealer}")
	keep_playing = input("Would you like to play again? yes or no?	").lower()
	if keep_playing == "yes":
		game()
	else:
		print("Ended")

game()