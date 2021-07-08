# Practise > Python > Strings > String Validators
# https://www.hackerrank.com/challenges/string-validators/problem

if __name__ == '__main__':
    s = input()

    list1 = ['True', 'True', 'True', 'True', 'True'] 

    if not s.isalnum():    # if the result is not true, then the condition is executed
        list1[0] = False

    if not s.isalpha():
        list1[1] = False

    if not s.isdigit():
        list1[2] = False

    if not s.islower():
        list1[3] = False

    if not s.isupper():
        list1[4] = False

    for result in list1:
        print(result)
