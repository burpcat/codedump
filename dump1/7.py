# Practise > Python > Strings > Strings split and Join

def split_and_join(line):
    splitline = line.split()
    cutline = "-".join(splitline)
    return cutline

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
