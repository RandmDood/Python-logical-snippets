import random
words_list = [
    "orchard", "balloon", "holiday", "cabinet", "traffic", "density", 
    "blanket", "journal", "silence", "circuit", "terrain", "sunrise", 
    "journey", "picture", "respect", "sandals", "justice", "perfume", 
    "library", "concert", "physics", "biscuit", "fortune", "process", 
    "chicken"
]
blan = []
blank = ""
fails = 8
word = random.choice(words_list)
print("HANGMAN GAME\nGUESS THE WORD")
print(f'hint: the word starts with a "{word[0].upper()}" and ends with a "{word[-1].upper()}" ')
for w in word:
	blan.append("*")
fact = 0
factno = 0
guess = ""
while fails != 0 and blan != word:
	hg = input("\nguess a letter:   ")
	guess = hg.lower()
	for n in range(0, len(blan)):
		if guess == word[n]:
			blan[n] = guess
			factno += 1
		if factno > 0:
			fact = 1
		else:
			fact = 0
	if fact <= 0:
		fails -= 1
		print(f"Incorrect. you can fail only {fails} more times")
	factno -= factno
	
	for n in range(0, len(blan)):
		blank += str(blan[n])
	print(blank.upper())
	blank = ""

if blan != word:
	print("Game over.")
else:
	print("\nCONGRATULATIONS!\nyou win")
