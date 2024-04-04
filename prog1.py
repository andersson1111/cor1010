import numpy as np

arrayNumber = np.random.randint(0, 10, size=20)
print(arrayNumber)

# to make a group of unique numbers 
# Array = [5 9 9 3 9 4 1 2 8 3 3 7 3 8 9 8 4 4 8 0]
# unique_A = [1, 2, 5, 0, 8, 7, 4, 9, 3]
# array = '[]'

uniqueList = []
for number in arrayNumber:
    if number in uniqueList:
        pass
    else:
        uniqueList.append(number)
#
print("unique: ", uniqueList)

uniqueList2 = list() # []
for number in arrayNumber:
    if number not in uniqueList2:
        uniqueList2.append(number)
#
print("unique2: ", uniqueList2)

# uniqueList3 = [number for number in arrayNumber if number not in uniqueList3]

myList = []
myList2 = list()

#set, dict
uniqueSet = set()
for num in arrayNumber:
    uniqueSet.add(num)
#
print(uniqueSet)
for elem in uniqueSet:
    print(elem, end=' ')
print()