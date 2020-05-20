5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

# Code starts from here


numberList = []
i=-1
while True:
    i=i+1
    item = input()
    if item == 'done' :
        break
    try:
        itemm= int(item)
        numberList.append(itemm)
    except:
        print('Invalid input')
        continue
numberList.sort()
ab=len(numberList)


print("Maximum is", numberList[ab-1])
print("Minimum is" ,numberList[0])
