from itertools import permutations
a, b = [int(x) if x.isnumeric() else x for x in input().split()]
lst  = tuple(permutations(a, b))
for i in lst:
    j = ''.join(sorted(i))
    print(j, "\n")
