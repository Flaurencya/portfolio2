#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Create the list of words you want to choose from.
aList = [0, 1]

#Generates a random integer.

aRandomIndex = randint(0, len(aList)-1)
appetizer = ["gado gado", "siomay", "martabak", "rawon", 'baso goreng']
x = randint(0, len(appetizer)-1)
print("appetizer: ", appetizer[x])
entree = ["sate", "rendang", "sop buntut", "nasi uduk"]
y = randint(0, len(entree)-1)
print("entree: ", entree[y])
desert = ["es teler", "es campur", "durian"]
z = randint(0, len(desert)-1)
print("desert: ", desert[z])
#print random results in list
menu = [appetizer[x], entree[y], desert[z]]
for appetizer[x] in menu:
    print(appetizer[x])
