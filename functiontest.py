import numpy as py
import matplotlib.pyplot as plt
# function

def add(a, b,c):
    "a, b, c are all numbers: int, float"
    result = a + b + c
    return result

i = 1
j = 2
k = 3

z = add(i, j, k)
print(i, j, k, "=", z)



def getUniqueLetters(string):
    " string: a str type input"
    listofuniqueletters = []
    for ch in string:
        if ch not in listofuniqueletters:
            listofuniqueletters.append(ch)
    #

    return listofuniqueletters
#

myString = " I like spring."
myUniqueLetters = getUniqueLetters(myString)
print(myUniqueLetters)

myString2 = "Spring is good, winter is good, summer is good, autumn is very good."
myUL = getUniqueLetters(myString2)
print(myUL)

myUL2sorted = sorted(myUL)
print(myUL2sorted)
# reverse the sorted output

#
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

plt.plot(x, y)
plt.show()
