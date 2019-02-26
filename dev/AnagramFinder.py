import datetime
import sys

times = []
for i in range(1000):
    start = datetime.datetime.now()

    lenfn = len
    sortfn = sorted
    lower = str.lower

    wordToFindOriginal = lower(' '.join(sys.argv[2:]))
    wordToFind = sortfn(wordToFindOriginal)
    wordToFindLength = lenfn(wordToFindOriginal)

    foundAnagrams = []

    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()

    for word in lines:
        if(lenfn(word) == wordToFindLength):    
            word = lower(word)
            if(word != wordToFindOriginal):
                if(sortfn(word) == wordToFind):
                    foundAnagrams.append(word)
       
    finish = datetime.datetime.now()
    duration = finish - start
    times.append(duration.microseconds)
    #print(duration.microseconds, ','.join(foundAnagrams), sep=',')

print(sum(times) / float(len(times)))
 
