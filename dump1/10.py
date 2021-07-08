# Practise > Python > Strings > Mutations

# https://www.hackerrank.com/challenges/python-mutations/problem


def mutate_string(listIP, position, character):
    listIP = list(listIP)
    listIP[position] = character
    mainstring = ''
    for element in listIP:
        mainstring += element
    return mainstring


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
