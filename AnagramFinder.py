import datetime
import sys

start = datetime.datetime.now()

wordToFindOriginal = ' '.join(sys.argv[2:])
wordToFind = sorted(wordToFindOriginal)
wordToFindLength = len(wordToFindOriginal)

foundAnagrams = []

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

for word in lines:
    if(len(word) == wordToFindLength):    
        word = word.lower()
        if(word != wordToFindOriginal):
            if(sorted(word) == wordToFind):
                foundAnagrams.append(word)
   
finish = datetime.datetime.now()
duration = finish - start

print(duration.microseconds, ','.join(foundAnagrams), sep=',')

