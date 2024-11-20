letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['@', '#', '&', '₦', '?', '!', '£', '₱']
print(len(symbols))

num_letters = int(input("how many letters would you like in your password?\n "))
num_numbers = int(input("How many numbers would you like in your password?\n "))
num_symbols = int(input("How many symbols would you like in your password?\n "))

import random

let = []
for letter in range(0, num_letters):
	cut = random.randint(0, (len(letters) - 1))
	let.append(letters[cut])

num = []
for number in range(0, num_numbers):
	cut2 = random.randint(0, (len(numbers) - 1))
	num.append(numbers[cut2])

sym = []
for symbol in range(0, num_symbols):
	cut3 = random.randint(0, (len(symbols) - 1))
	sym.append(symbols[cut3])

total = let + num + sym
tot = ""
for t in total:
	i = str(t)
	tot += i

password = ""
ran = random.sample(range(len(tot)), len(tot))
for r in ran:
	password += tot[r]
print()
print(f"Your password is: {password}")