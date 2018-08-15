'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''
import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Textblob:
polarity = []
subjectivity = []

for idx in range(len(tweetData)):
    tb = TextBlob(tweetData[idx]["text"])
    pole= tb.polarity
    polarity.append(float(pole))
    sub = tb.subjectivity
    subjectivity.append(float(sub))

print("Polarity: " + str(polarity))
print("Subjectivity: " + str(subjectivity))
total = sum(polarity)
average = total/float(len(polarity))
print("The average is " + str(average))

#histogram
import matplotlib.pyplot as plt
#bins are increments
plt.hist(polarity)
plt.hist(subjectivity)
plt.xlabel('Polarity and Subjectivity')
plt.ylabel('Frequency')
plt.title('Histogram of Polarity')
plt.axis([-1.1, 1.1, 0, 120])
plt.grid(True)
plt.show()
