filename = "pride.txt"
#filename = "num.txt"

filehandler = open(filename, "r", encoding='utf-8')

n = 0
ulist = []
while True:
    line = filehandler.readline()
    if not line:
        break
    n += 1
    for letter in line:
        if letter not in ulist:
            ulist.append(letter)
    #print (n, line)
    #if n > 3:
    #   break
#
            
print(n, len(ulist), ulist)

f2 = open("prog1.py", "r")
n = 0
while True:
    line = f2.readline()
    if not line:
        break #get out of the while-loop
n += 1
print(n, line)