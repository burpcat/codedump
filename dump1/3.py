# Hackerrank
# Python
# Find the Runner-Up Score!

def sorever(arr1):
    arr1.sort()
    arr1.reverse()
    return arr1


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    newarr = sorever(arr)
    print(newarr)
    anList = []
    for i in newarr:
        if i not in anList:
            anList.append(i)
    print(anList)

    print(anList[1])
