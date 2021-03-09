import random

def computer_guess(x):
	low = 1
	high = x
	feedback = ''
	while feedback != 'c':
		if low != high:
			guess = random.randint(low, high)
		else:
			guess = low 
		feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)?? ").lower()
		if feedback == 'h':
			high = guess - 1
		elif feedback == 'l':
			low = guess + 1

	print(f"\nThe computer guessed your number {guess} correctly!")

def replay():
    answer = input('Do you want to play again? Enter yes or no: ').lower()
    return answer =='yes'

print("You're playing a guessing game with the computer! Pick any whole number between 1 and 100 right \
now and the computer will start guessing your number. Let the computer know if their guess is too high, \
too low, or correct! \n")


while True:
	start_game = input("Are you ready to play? Enter yes or no: ").lower()
	if start_game == 'yes':
		play_game = True
	else:
		play_game = False
	
	while play_game:
		computer_guess(100)
		play_game = False


	if not replay():
		break