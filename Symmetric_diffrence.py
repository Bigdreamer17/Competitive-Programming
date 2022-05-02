fsize = int(input("Enter size of the first set: "))
lst = list(map(int, input("Enter set values: ").split()))
s1 =  set()
ssize = int(input("Enter size of the second set: "))
lst2 = list(map(int, input("Enter set values: ").split()))
s2 = set()
if len(lst) > fsize and len(lst2) > ssize:
    print("Out of range!!") 
else:
    s1.update(lst)
    s2.update(lst2)
c = s1.symmetric_difference(s2)
for i in c:
    print(i)


