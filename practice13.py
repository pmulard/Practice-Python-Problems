#Python practice 13 - Fibonacci
#Ask the user how many Fibonnaci numbers to generate then generate them.generate

#Asks user input and sets fib value for 1 (because program can't add to non existing 2nd value)
userInput = int(input('Give me a number... Any number... '))
if userInput == 1:
	fib = [1]

#Sets the sequence for 2+ values and prints the final list.
elif userInput != 1:
	fib = [1,1]
	for n in fib:
		if len(fib) < userInput:
			n = fib[-1] + fib[-2]
			fib.append(n)
print(fib,)

