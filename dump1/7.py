# Practise > Python > Strings > Strings split and Join
# https://www.hackerrank.com/challenges/python-string-split-and-join/problem

def split_and_join(line):
    splitline = line.split()
    cutline = "-".join(splitline)
    return cutline

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
