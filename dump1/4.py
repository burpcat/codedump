# Hackerrank
# Python3
# What's Your Name?


def print_full_name(first, last):
    return (first+' '+last)


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    finalstr = print_full_name(first_name, last_name)
    print(f'Hello {finalstr}! You just delved into python.')
