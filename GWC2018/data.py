import json
from pprint import pprint


# Open a json file and append entries to the file.
f = open("allanswers.json", "r")
data = json.load(f)
print(type(data))
print(data)
f.close()

age = []
for s in range(len(data)):
    age.append(int(data[s]['age']))
print(age)
total = sum(age)
average = total/len(age)
print(average)

count = []
blueCount = 0
notBlueCount = 0
for c in data:
    if c['color'] == "blue":
        count += 1
    else:
        notBlueCount += 1
print("The number of blues is " + str(blueCount))
print("The number of non blues is " + str(notBlueCount))
