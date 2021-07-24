# Practise > Python > Sets > Introduction to Sets
# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem


def average(array):
    # your code goes here
    sumnum = 0
    mainSet = set(array)
    for i in mainSet:
        sumnum = sumnum + i

    return (sumnum/len(mainSet))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
