# Practise > Python > Basic data types > nested lists
# https://www.hackerrank.com/challenges/nested-list/problem


mainList = []
totNum = int(input())   # Number of members

for val in range(totNum):
    subList = []
    for i in range(2):
        inVal = input()
        subList.append(inVal)
        print(subList)
    mainList.append(subList)
    print(mainList)

for lism in mainList:
    lism[0], lism[1] = lism[1], lism[0]

mainList.sort()
print(mainList)
#secLow = mainList[1][0]
meagLow = mainList[0][0]
countr = 0

print(mainList)

while True:
    for i in range(len(mainList)):
        if mainList[i][0] == meagLow:
            print(mainList[i][0], meagLow)
            continue
        else:
            secLow = mainList[i][0]
            print(secLow)
        break
    break

while True:
    for i in range(len(mainList)):
        if mainList[i][0] == secLow:
            print(mainList[i][1])
    break
