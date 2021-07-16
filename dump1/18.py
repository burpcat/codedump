# Practise > Python > Itertools > itertools.product()
# https://www.hackerrank.com/challenges/itertools-product/problem

from itertools import product
mainstr = ''


def intconv(numlist):
    return list(map(int, numlist))


num1 = intconv(input().split())
num2 = intconv(input().split())
#print(num1, num2)

mainList = list((product(num1, num2)))
print(*mainList)

#    (or)
# Instead of using the above print(*mainlist), we can use the below code
# for num in mainList:
#    mainstr = mainstr + str(num) + ' '
# print(mainstr)
