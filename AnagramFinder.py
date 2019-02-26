import datetime
import sys

start = datetime.datetime.now()

lenfn = len
sortfn = sorted

wordToFindOriginal = ' '.join(sys.argv[2:])
wordToFind = sortfn(wordToFindOriginal)
wordToFindLength = lenfn(wordToFindOriginal)

foundAnagrams = []

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

for word in lines:
    if(lenfn(word) == wordToFindLength):    
        word = word.lower()
        if(word != wordToFindOriginal):
            if(sortfn(word) == wordToFind):
                foundAnagrams.append(word)
   
finish = datetime.datetime.now()
duration = finish - start

print(duration.microseconds, ','.join(foundAnagrams), sep=',')

 
