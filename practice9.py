#Practice python exercise 9 - Guess the number
#Generate a random number from 1-10 and have user try to guess the number

#Generates a random number, gives user instructions, and sets turn counter
import random
ranNum = random.choice(range(1,11))
print('Guess a number between 1 and 10... (Type exit to quit.)')
counter = 0

while True:
	#Asks user to guess the number
	guess = input('What\'s your guess? ')

	#Validates guesses by the user and if they want to quit
	if guess.lower() == 'exit':
		print('Winners never quit...')
		break
	elif int(guess) == ranNum:
		counter += 1
		
		#Fixes grammar if user guesses in 1 'try' or several 'tries'
		if counter == 1:
			print('You got it! It took you 1 try!')
		else:
			print('You got it! It took you {} tries.'.format(counter))
		break
	elif int(guess) > ranNum:
		counter += 1
		print('Lower.')
	elif int(guess) < ranNum:
		counter += 1
		print('Higher.')
