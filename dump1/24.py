# Practise > Python > Sets > Symmetric Difference
# https://www.hackerrank.com/challenges/symmetric-difference/problem

finalSet = set()

firstInp = input()
firstSet = set(list(map(int, input().split())))

secondInp = input()
secondSet = set(list(map(int, input().split())))

finalSet.update(firstSet.difference(secondSet))
finalSet.update(secondSet.difference(firstSet))

for i in sorted(finalSet):
    print(i)
