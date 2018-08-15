# --- Define your functions below! ---
def intro():
    print("Hi! I'm chatbot!")

def response(answer2):
    if answer2 == "hi":
        print("Hi, how you doing?")
    else:
        print("That's cool!")
# --- Put your main program below! ---
def main():
    intro()
    while True:
        answer1 = input("What will you say? ")
        response(answer1)


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
