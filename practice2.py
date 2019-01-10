#Exercise 2 - Odd or Even
#Asks the user for a number, then determines whether it is even or odd

#Asks the user for a number and provides an output message if it isn't an integer
try:
	n = int(input("Hey there! Give me a number, any number...   "))
except:
	print('You did not provide a valid number.')

#Creates a function that determines if it's odd or even. It also calculates if it's a
#multiple of 4.
def evenOdd():
	if n % 2 == 0 and n % 4 != 0:
		print("Looks like you have an even number.")
	elif n % 4 == 0:
		print("This is even, and it\'s a multiple of four too.")
	else: 
		print("Looks like your number is odd. Kinda like you... ")

evenOdd()