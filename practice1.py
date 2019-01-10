#Exercise 1 - Character Input
#Ask user to enter name and age. Print out what year they'll turn 100.

#Gets name and age from user
userName = input("What is your name? ")
userAge = int(input("How old are you? "))

#Calculates the current year and the year the user turns 100, which then prints it out.
from datetime import date
currentYear = int(date.today().year)
centuryYear = (100 - userAge) + currentYear
century = ("{}, you will be 100 on {}.".format(userName,centuryYear))
print(century)

#Asks user for a random number, then prints the previous message however many times the number is.
randomNumber = int(input("OK {} give me a random number between 1 and 10. ".format(userName)))
century += "\n"
print(century * randomNumber)