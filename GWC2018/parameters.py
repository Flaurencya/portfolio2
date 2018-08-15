#transfering variables using parameters
def hello(name):
    print("hello" + name)
def books(book):
    book = input("What is your favorite book?")
    print(book + ", is a great suggestion!")
def goodbye(name2):
    print("hello" + name2)
def main():
    user = input("What's your name?")
    hello(user)
#you must cite a parameter for the books functions
    books(user)
    goodbye(user)


if __name__ == "__main__":
  main()
