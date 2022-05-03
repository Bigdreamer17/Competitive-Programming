a , b = [int(a) for a in input().split()]
lst = list(map(int, input().split()))
if len(lst) > a:
    print("Out of Range!!!")
c , d = [int(c) for c in input().split()]
e, f = [int(e) for e in input().split()]
i = 0 
if c in lst:
    i += 1
if d in lst:
    i += 1   
if e in lst:
    i -= 1
if f in lst:
    i -= 1
print (i)      