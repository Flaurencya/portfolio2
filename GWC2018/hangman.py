word = [input("Choose a word to begin with")]
_ = blanks = len(word)
success = [_, _, _, _, _, _, _]
attempts = 6

while(attempts != 0):
    print("There are 7 spaces, and no repeating letters, good luck!")
    guess = input()
#checking if the guess is matching and how to place it in the right blank
    if guess in word:
        for i in range(len(word)):
            if guess == word[i]:
                success.append("guess")
                blanks -= 1
                print("You have successfully guessed," + len(succ   ess) + ",numbers out of,"+ len(word))
        if "_" not in success:
            print("Yay you win!")
            break
    elif(guess in word == False):
        failed = []
        failed.append(guess)
        attempts -= 1
        print("You have", attempts, "left. Try again.")
        print("You have successfully guessed", + len(success) + ",numbers out of", len(word))
