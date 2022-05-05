from itertools import combinations
a, b = [int(x) if x.isnumeric() else x for x in input().split()]
lst  = tuple(combinations(a, b))
for i in lst:
    j = ''.join(sorted(i))
    print(j, "\n")