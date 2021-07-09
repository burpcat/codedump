# Practise > Python > Collections > Company Logo
# https://www.hackerrank.com/challenges/most-commons/problem

import collections
mainstring = sorted(input())
orderColl = collections.Counter(mainstring).most_common(3)   # Using the collections module, we can calculate the most common
for i, j in orderColl:
    print(i, j)
