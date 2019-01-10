#Practice python 14 - List Remove Duplicates
#Takes a list and returns a new list that contains all the elements of the first list
#minus any duplicates.import

#Creates a random list and converts to a set (this automatically removes duplicates). 
#Then converts back into list to keep in spirit with instructions.
import random
oldList = list(set(random.choices(range(1,11), k = 10)))
print(oldList)

#This function uses a loop to construct the new list for a different approach.
def loop(a):
	newList = []
	for i in a:
		if i not in newList:
			newList.append(i)
	print(newList)

a = [1, 1, 2, 4, 4, 4, 5, 6, 8, 8, 9, 10, 10, 10]
b = [2, 2, 3, 4, 5, 6, 6, 6, 10, 10]
loop(a)
loop(b)

#This is a variation of the 1st approach, but uses a function instead.
def removeDup(a):
	newNewList = list(set(a))
	print(newNewList)
removeDup(b)