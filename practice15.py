#Practice python exercise 15 - Reverse Word Order
#Use functions to ask the user for a long string w/ multiple words and print
#the string with the words in reverse order.

#Asks the user for a string, then splits the string by whitespace (leaving blank).
#Takes reversed items and then creates a list. Note - using reversed method by 
#itself will not return a list, hence the list method being used.
def revWords():
	string = input('What is a sentence you would like to say? ')
	newList = list(reversed(string.split()))
	print(newList)
revWords()

