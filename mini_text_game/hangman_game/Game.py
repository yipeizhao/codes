import json
import string
import random
with open('dictionary.json') as f:
	words = json.load(f)
f.close()

while True:
	flag = True
	word = random.choice(list(words.keys()))
	word_def = words[word]
	print(word_def)
	heart = 8
	print("You have " + str(heart) + " hearts left." + "♥"*heart)
	charas = [string.ascii_uppercase]

	# Happens in one round/guess
	while flag:
		hidden = ["_"]*len(word)
		print(" ".join(hidden))
		print("/".join(charas))
		guess = input("Your guess guess is:")
		index = []
		for i in range(len(word)):
			if word[i]==guess:
				index.append(i)
		if len(index)!=0:
			print("The letter " + guess + " is in the word.")
			for i in index:
				hidden[i] = guess
		else:
			print("The letter " + guess + " is not in the word.")
			heart-=1
		print("You have " + str(heart) + " hearts left." + "♥"*heart)
		print(" ".join(hidden))


	# Game start
	# Set score
	# Load dict
		# Choose a word, and load definition
		# Hide the word
			# Print info
			# Ask for input
				# If correct
				# Print new info
				# Else
				# Lose a heart
				