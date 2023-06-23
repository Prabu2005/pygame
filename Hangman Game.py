import random

# function for hangman
def hang(n):
	if n == 1:
		print("\n O \n | ")
	elif n == 2:
		print("\n O \n |/")
	elif n == 3:
		print("\n O \n\\|/")
	elif n == 4:
		print("\n O \n\\|/\n/")
	else:
		print("\n O \n\\|/\n/ \\")
		print("\n\nYou ran out of choices, you are being hanged!")

words = ["beautiful", "excellent", "great", "underneath"]

find_word = random.choice(words)
find_word_len = len(find_word)

word = []
i = 1
while(i<=find_word_len):
	word.append(" _ ")
	i = i + 1

TRY = 0
while (TRY<5):
	print("\n", "".join(word))
	if "".join(word) == find_word:
		print("\nYOU WON!")
		exit(0)

	letter = input("\n\nChoose a letter: ")

	if letter == find_word:
		print("\nYOU WON!")
		exit(0)

	pos_list = []
	if letter in find_word:
		l = -1
		while True:
			l = find_word.find(letter, l+1)
			if l == -1:
				break
			pos_list.append(l)
	else:
		TRY = TRY + 1
		hang(TRY)
	
	for i in pos_list:
		word[i] = letter
