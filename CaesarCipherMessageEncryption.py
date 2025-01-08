letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
word = input("Enter any message\n").lower()
shift = int(input("Enter your shift value"))
result = ""

def encrypt(a, b):
	global result
	global letters
	for let in word:
		pos = letters.index(let)
		if b + pos < len(letters):
			letters[pos] = letters[b + pos]
		else:
			newpos1 = -pos
			letters[pos] = letters[newpos1]
		result += letters[pos]
		letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	print(f"here is your encrypted message: {result}")

def decrypt(c, d):
	resultB = ""
	global letters
	for let in c:
		pos2 = letters.index(let)
		if pos2 - d > 0:
			letters[pos2] = letters[pos2 - d]
		else:
			newpos = -pos2
			letters[pos2] = letters[newpos]
		resultB += letters[pos2]
		letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	print(f"here is your decrypted message: {resultB}")
	
encrypt(word, shift)
decrypt(result, shift)
	
