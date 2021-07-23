# Practise > Python > Errors and Exceptions > Errors
# https://www.hackerrank.com/challenges/exceptions/problem

n = int(input())

for i in range(n):
    #a, b = map(int, input().split())
    a, b = input().split()
    try:
        print(int(a)//int(b))
    except ZeroDivisionError as e:
        print(f'Error Code: {e}')
    except ValueError as e:
        print(f'Error Code: {e}')
