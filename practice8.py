#Practice python exercise 8
#Make a 2 player rock paper scissors game

import random
quitNotice = print('Ctr + c to exit game.')

while True:
	selection = input('\nrock, paper or scissors? ')
	computer = random.choice(['rock', 'paper', 'scissors'])
	if selection.lower() == computer:
		print('It\'s a tie!')
	elif selection.lower() == 'rock' and computer == 'scissors':
		print('Rock beats scissors, you win!')
	elif selection.lower() == 'rock' and computer == 'paper':
		print('Paper beats rock, you lose!')
	elif selection.lower() == 'paper' and computer == 'rock':
		print('Paper beats rock, you win!')
	elif selection.lower() == 'paper' and computer == 'scissors':
		print('Scissors beats paper, you lose!')
	elif selection.lower() == 'scissors' and computer == 'paper':
		print('Scissors beats paper, you win!')
	elif selection.lower() == 'scissors' and computer == 'rock':
		print('Rock beats scissors, you lose!')