#Practice python exercise 6 - Palindrome check

userStr = input('Input a string that you think is a palindrome. I\'ll give you a hint - MADAM is one: ')
print(userStr[::-1])
if userStr == userStr[::-1]:
	print('That\'s a palindrome!') 
else:
	print('Unfortunately that is not a palindrome.')

