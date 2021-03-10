import random
from words import words
import string

def get_valid_word(words):
	word = random.choice(words)
	while '-' in word or ' ' in word:
		word = random.choice(words)
	return word.upper()

def hangman():
	word = get_valid_word(words)
	letters_in_word = set(word)  # letters in the word
	alphabet = set(string.ascii_uppercase)
	used_letters = set()  # used letters that user has guessed

	lives = 8

	while len(letters_in_word) > 0 and lives > 0:
		print('\nYou have', lives, 'lives left and guessed these letters already: ', ' '.join(used_letters))

		word_list = [letter if letter in used_letters else '-' for letter in word]
		print('Guess this word: ', ' '.join(word_list))

		guess_letter = input('Guess a letter: ').upper()
		if guess_letter in alphabet - used_letters:
			used_letters.add(guess_letter)
			if guess_letter in letters_in_word:
				letters_in_word.remove(guess_letter)

			else:
				lives = lives - 1
				print('\nThe letter you guessed is not in the word.')

		elif guess_letter in used_letters:
			print('\nYou have already used that character. Please try again.')

		else:
			print('\nInvalid character. Please try again.')

	if lives == 0:
		print('\nSorry, you died. The word was', word)
	else:
		print('You guessed the word', word, '!!')

hangman()