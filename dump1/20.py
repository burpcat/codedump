# Practise > Python > Itertools > itertools.permutations()
#

from itertools import permutations

inp_string = input()
wordLis, numa = inp_string.split()


print(*[''.join(item) for item in list(permutations(sorted(wordLis), int(numa)))], sep='\n')


