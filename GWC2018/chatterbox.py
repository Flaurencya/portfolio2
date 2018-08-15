colors = ["green", "blue", "purple", "brown"]
numbers = [1,2, 3, 4, 5, 6, 7, 8]
def main():
    answer = input("Choose a color from green, blue, purple, brown")
    if (answer == "green") or (answer == "brown"):
        odd = oddnumberchoice()
        if odd == "1":
            choice1()
        if odd == "2":
            choice2()
        if odd == "5":
            choice5()
        if odd == "6":
            choice6()
    elif (answer == "purple") or (answer == "blue"):
        even = evennumberchoice()
        if even == "3":
            choice3()
        if even == "4":
            choice4()
        if even == "7":
            choice7()
        if even == "8":
            choice8()

def oddnumberchoice():
    return input("Choose a number from 1,2,5, or 6")
def evennumberchoice():
    even = input("Choose a number from 3,4,7, or 8")
def choice1():
    print("You will meet your favorite artist")
def choice2():
    print:("You will break a mirror")
def choice3():
    print:("Beware of the pigeons")
def choice4():
    print:("Sorry, try again")
def choice5():
    print("You will win a lot of money")
def choice6():
    print:("You will find an ant in the folds of your right ear")
def choice7():
    print("You will miss your trian")
def choice8():
    print("You will step on dog poop")

if __name__ == "__main__":
    main()
