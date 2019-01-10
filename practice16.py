#Python practice 16 - Password Generator
#Generate a password with a mix of upper and lowercase letters, numbers, and symbols. 
#Ask user how strong password should be and include the run-time code in a main method.

def main():
	
	def passwordGenerator():
		
		#Defines the content that will make up the passwords
		import random
		adjective = ['Small', 'Big', 'Dumb', 'Hungry', 'Thirsty', 'Smart', 'Excellent', 'Local', 'Foreign', 
					 'Strong', 'Weak', 'Special', 'Old', 'Young', 'Violent', 'Lazy' ]
		color = ['Blue', 'Red', 'Green', 'Purple', 'Yellow', 'Orange', 'Pink', 'Magenta', 'Violet']
		animal = ['Lion', 'Elephant', 'Tiger', 'Penguin', 'Orca', 'Bear', 'Swordfish', 'Antelope', 'Alligator',
				  'Eagle', 'Seagull', 'Squirrel', 'Rabbit']
		noun = ['Eater', 'Killer', 'Rider', 'Stuffer', 'Owner', 'Petter', 'Watcher', 'Lover']
		symbol = ['!', '@', '#', '$', '%', '^', '^', '&', '*']

		#Creates 3 passwords with varrying strengths. The last 2 contain a random set of numbers and symbols respectively.
		passStrength = input('Do you want a standard, strong or very strong password? Type answer: ')
		standardPassword = str(random.choice(adjective) + random.choice(color) + random.choice(animal) + random.choice(noun))
		strongPassword = standardPassword + "-" + ''.join(map(str,random.choices(range(1,9), k = 4 )))
		veryStrongPassword = strongPassword + "-" + ''.join(map(str,random.choices(symbol, k = 3)))

		#Conditionals to output the corresponding password depending on the user's input.
		if passStrength == 'standard':
			print('Your new password is {}'.format(standardPassword))
		elif passStrength == 'strong':
			print('Your new password is {}'.format(strongPassword))
		elif passStrength == 'very strong':
			print('Your new password is {}'.format(veryStrongPassword))
		else:
			print('Please read the instructions and try again.')

	passwordGenerator()


	#Password generator for a more simplistic and randomized set
	def passGen():
		import random
		symbol = ['!', '@', '#', '$', '%', '^', '^', '&', '*']
		letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q',
		          'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
		str1 = ''.join(map(str, random.choices(range(1,10), k = 4)))
		str2 = ''.join(map(str, random.choices(letter, k = 5))) + random.choice(symbol)
		str3 = ''.join(map(str, random.choices(range(1,10), k = 4))) + random.choice(symbol)
		print(str1 + "-" + str2 + "-" + str3)

	passGen()


	#Another approach...
	def easyPass():
		import random
		upperL = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		lowerL = 'abcdefghijklmnopqrstuvwxyz'
		symbols = '!@#$%^&*~+='
		numbers = '123456789'

		password = ''
		password += random.choice(upperL)
		password += random.choice(upperL)
		password += random.choice(lowerL)
		password += random.choice(upperL) + '-'
		password += random.choice(numbers)
		password += random.choice(numbers)
		password += random.choice(numbers)
		password += random.choice(numbers)
		password += random.choice(symbols)
		print(password)

	easyPass()


	#And another super simple password with only numbers - 8 digits
	import random
	def superSimplePassword():
		password = ''
		for i in range(0,8):
			password += str(random.randint(0,10))
		print(password)

	superSimplePassword()

main()