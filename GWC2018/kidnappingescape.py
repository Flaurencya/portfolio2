HP = 100
name = input("What's your name?")
print("Sorry,", name, ",you have been kidnapped. Make the right choices and escape!")
start = '''
When you wake, you find your arms and legs bound to a rickety wooden chair in a cabin.
Outside you smell pine and the light indicates midday.
'''
print(start)
print("Quick! Decide how to get out of the chair, either smash the chair or wiggle out. Type 'smash' or 'wiggle'.")
chair = input()
if (chair == "smash"):
    print("In smashing the chair against a wall you got splinters all over and bled out 25HP")
    HP -= 25
elif (chair == "wiggle"):
    print("In wiggling out you got some rope burn but got out unscathed")
print("Do you leave the cabin by going left or right? Type 'left' or 'right'.")
direction = input()
if(direction != "left" or direction != "right"):
    print("You can't go," +direction+ ", try again")
elif(direction == "left"):
    print("Taking the pebbly path left takes you deeper into the wood, where you encounter a grizzly bear!")
    print("Quick! Do you fight the bear with an axe lying nearby? Type 'yes' or 'no'.")
    fight = input()
    if(fight == "yes"):
        print("The bear is ahead of you and suddenly mauls you and the axe falls out of your hand and you die.")
        HP -= 25
        print(HP)
    elif(fight == "no"):
        print("You run away and survive")
        highway = input()
elif(highway == "right"):
    print("You reach the highway. Quick! Do you flag down the chicken truck or the sedan? Type 'sedan' or 'truck'")
    if(highway == "truck"):
        print("The old man helps you call 911 and get away. Congratulations!")
    elif(highway == "sedan"):
        print("You approach the lady and get into the car. The car locks and suddenly you smell chloroform and pass out. When you wake you find yourself in the cabin once again.")
        HP -= 25
        print(HP)
