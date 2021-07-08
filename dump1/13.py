# Practise > Python > Strings > String Validators
# https://www.hackerrank.com/challenges/string-validators/problem

if __name__ == '__main__':
    s = input()
    print(f'{any(map(str.isalnum,s))}\n{any(map(str.isalpha,s))}\n{any(map(str.isdigit,s))}\n{any(map(str.islower,s))}\n{any(map(str.isupper,s))}\n')

    # any() function returns true even if one functin is true in the list or dictionaru
