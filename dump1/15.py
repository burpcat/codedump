# Practise > Python > Basic Data Types > List comprehensions
# https://www.hackerrank.com/challenges/list-comprehensions/problem

x = int(input())
y = int(input())
z = int(input())
n = int(input())

mainlist = []
for a in range(0, x+1):
    for b in range(0, y+1):
        for c in range(0, z+1):
            subList = [a, b, c]
            if not subList in mainlist and not a+b+c == n:
                mainlist.append(subList)

print(mainlist)
