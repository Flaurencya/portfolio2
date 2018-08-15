import json

def survey ():
    answers = {}
    # TODO Part I: Add your survey questions to this empty list.
    survey = ["What's your age?", "What's your favorite book?", "What's your favorite color?", "What is your favorite word?", "What is your all-time favorite movie?"]

    # TODO Part I: store the related keys corresponding to the survey answers here.
    keys = ["age", "book","color","word","movie"]

    # TODO Part I: write code that asks each survey question and prompts the user for a response.
    # Hint: how can you go through each element of a list?
    for i in range(len(survey)):
        #input from each of the survey questions as i goes through the loop
        answer = input(survey[i])
        #add answer into the dictionary
        answers[keys[i]] = answer
    return answers

#going through and repeating the process for each i, when i is equal to the range of the length of the list

list_of_answers = []
def main ():
    # Create a list that will store each person's individual survey responses.
    # Use for Part II.
    choice = input("How many people, including you, do you want to allow to take this survey?")
    choice = int(choice)
    while(choice > 0):
        list_of_answers.append(survey())
        choice -= 1
    print(list_of_answers)

if __name__ == "__main__":
    main()
# Print the context of the dictionary.

#TODO Part II: Delete the quotes. This will print each individual's survey responses
"""
#Example of how to iterate over the list of dictionaries and pull out particular pieces of information.
names = []
for s in range(len(list_of_answers)):
    names.append(list_of_answers[s]["name"])
print(names)
"""



# Open the file containing all past results and append them to our current list.
f = open("allanswers.json", "r")
olddata = json.load(f)
list_of_answers.extend(olddata)
f.close()

# Reopen the file in write mode and write each entry in json format.
f = open("allanswers.json", "w")
f.write('[\n')
index = 0
for t in list_of_answers:
    if (index < len(list_of_answers)-1):
        json.dump(t, f)
        f.write(',\n')
    else:
        json.dump(t, f)
        f.write('\n')
    index += 1

f.write(']')
f.close()
