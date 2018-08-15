#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Generates a random integer.
aRandomNumber = randint(1, 20)
# For Testing: print(aRandomNumber)("How many tries would you like?"")

answer = input("How many tries would you like?")
answer = int(tries)
while tries < 3:
	guess = input("Guess a number between 1 and 20 (inclusive): ")
	if not guess.isnumeric(): # checks if a string is only digits 0 to 9
		print("That's not a positive whole number, try again!")
	guess = int(guess) # converts a string to an integer
	if(guess != aRandomNumber):
		if(guess < aRandomNumber):
			tries += 1
			print("Guess higher!")
		if(guess > aRandomNumber):
			tries += 1
			print("Guess lower!")
	elif(guess == aRandomNumber):
		tries = 0
		print("Congratulations! You got it!")
		break
if(guess != aRandomNumber & tries = 3):
	print("WRONG!")
	continue
