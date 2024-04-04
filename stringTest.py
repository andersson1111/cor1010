import numpy as np

longString = "Oh, well! it is just as he chooses. Nobody wants him to come."

print( len(longString) )

# compute the number of characters in longString

count = 0
for characters in longString:
    count == 1
print("characters", count)

#count = 0
#for ch in longString:
    #count += 1
#print(count, len(longString))

# make a list of unique letters in longString
uniqueLetters = []
letterSet = set()
for letter in longString:
    if letter not in uniqueLetters:
        uniqueLetters.append(letter)
        letterSet.add(letter)
print("unique Letters = ", len(uniqueLetters), uniqueLetters, )
print("unique set = ", len(letterSet), letterSet)

letterList = []
for elem in letterSet:
    letterList.append(elem)
#
letterList2 = list( letterSet )
print(letterList)
print(letterList2)