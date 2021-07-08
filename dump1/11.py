# Practise > Python > Strings > Find a string
# https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(string, sub_string):
    count = 0
    # the range variable consists of how many times we can iterate over the main string with the length of the substring
    for i in range(0, len(string) - len(sub_string)+1):
        if string[i:i+len(sub_string)] == sub_string:
            # [i:i+len(sub_string)] -> parts of mainstring is measured against the substring
            count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
