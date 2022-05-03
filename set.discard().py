number_size = int(input("Enter size of set: "))
lst = []
if len(lst) > number_size:
    print("Out of range!!")
else:
    lst = list(map(int, input("Enter set values: ").split()))
s = set(lst)
N = int(input("Enter number of commands: "))
def pop(num):
    return s.pop()
def remove(num):
    return s.remove(num)
def discard(num):
    return s.discard(num)
for i in range(N):
    a, b = [int(x) if x.isnumeric() else x for x in input().split()]
    if a == 'pop':
        pop(b)
    if a == 'remove':
        remove(b)
    if a == 'discard':
        discard(b)
print("The set is now: ", s)
new_lis = list(s)
Sum = sum(new_lis)
print("The sum is: ", Sum)
  
