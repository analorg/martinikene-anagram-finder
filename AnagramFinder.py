import time
import sys

start = time.time()

lenfn = len
sortfn = sorted
lower = str.lower

wordToFindOriginal = lower(' '.join(sys.argv[2:]))
wordToFind = sortfn(wordToFindOriginal)
wordToFindLength = lenfn(wordToFindOriginal)

foundAnagrams = []

with open(sys.argv[1]) as f:
    lines = f.read().split('\n')

for word in lines:
    if(lenfn(word) == wordToFindLength):    
        word = lower(word)
        if(word != wordToFindOriginal):
            if(sortfn(word) == wordToFind):
                foundAnagrams.append(word)
   
finish = time.time()
duration = round((finish - start)*1000000, 2)

print(duration, ','.join(foundAnagrams), sep=',')

