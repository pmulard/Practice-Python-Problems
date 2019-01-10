#Practice python exercise 7
#Takes existing list and makes new list with only even numbers.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(a)

#By printing in one line instead of creating new list b, the b list is not stored in memory.
print([number for number in a if number % 2 == 0]) 

#If wanting to store new list b for further use:
b = [number for number in a if number % 2 ==0]
print(b)