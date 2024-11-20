import random
play = input("Virtual rock paper scissors\nMake any move between rock, paper, or scissors\n").lower()
r = "rock"
p = "paper"
s = "scissors"
hands = ["rock", "paper", "scissors"]
cp = random.randint(0, 2)
complay = hands[cp]
print(f"The computer picked {complay}")
if play == r and complay == hands[1]:
	print("Paper covers rock. You lose")
if play == r and complay == hands[2]:
	print("Rock beats scissors. You win")
if play == p and complay == hands[0]:
	print("Paper covers rock. You win")
if play == p and complay == hands[2]:
	print("Scissors cut paper. You lose.")
if play == s and complay == hands[0]:
	print("Rock beats scissors. You lose")
if play == s and complay == hands[1]:
	print("Scissors cut paper. You win.")
if play == complay:
	print("Draw")