# Practise > Python > Collections > collections.Counter()

from collections import Counter
shoesNum = int(input())     # Number of shoes in shop
profits = 0
sizes = input()             # Available sizes in the form of a string continuosly

cstNum = int(input())       # Number of customers

sizesList = sizes.split()
sizesList = list(map(int, sizesList))
sizeDict = dict(Counter(sizesList))      # returns the number of sizes
mylistkey = list(sizeDict.keys())


while cstNum:       # if zero -> false, else any positive number -> true
    askList = input()
    askList = askList.split()
    size = int(askList[0])
    price = int(askList[1])

    if size in mylistkey:   # To prevent non existing sizes to enter into loop
        if(sizeDict[size] != 0):
            sizeDict[size] -= 1
            # print(sizeDict)
            profits = profits + price
            #print(f'profits are {profits}')
        # else:
            #print('Outta stock')
    cstNum -= 1            # Control the while loop

print(profits)
