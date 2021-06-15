# Hackerrank
# Python3 > Basic Data Types
# Finding the Percentage

if __name__ == '__main__':
    n = int(input())
    maindict = {}

    for cab in range(n):
        mainstr = input().split()
        average = (float(mainstr[1])+float(mainstr[2])+float(mainstr[3]))/3
        # Using precision handling from Python
        format_average = "{:.2f}".format(average)
        maindict[mainstr[0]] = format_average

print(maindict[input()])
