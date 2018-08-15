#Opens a file. You can now look at each line in the file individually with a statement like "for line in f:
f = open("dictionary.txt","r")

print("Can your password survive a dictionary attack?")

#Take input from the keyboard, storing in the variable test_password
#NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords

test_password = input("Type in a trial password: ")
match = 0
good_password = False
while (good_password == False):
    for i in f:
        bad_password = i.strip()
        test_password = test_password.strip()
        if test_password == bad_password:
            match += 1
            print("That's a weak password! Please change it.")
            continue
        elif bad_password != test_password:
            match += 0
            good_password = True
            print("Congratulations, that's a strong password!")
            break
