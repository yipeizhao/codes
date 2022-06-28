import json
import random
with open('dictionary.json') as f:
	words = json.load(f)
f.close()

while True:
	word = random.choice(list(words.keys()))
	word_def = words[word]
	print("You have 8 hearts left. ♥♥♥♥ ♥♥♥♥")
	hidden = ""
	for i in range(len(word)):
		hidden += "_ "
	print(hidden)
	print(word_def)
	print("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z")
	

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
				