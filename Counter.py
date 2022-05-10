from collections import Counter
num_shoe = int(input("Enter number of shoes: "))
shoe_size = list(map(int, input("Enter number of shoe size: ").split()))
if len(shoe_size) > num_shoe:
    print ("Out of range!!!")
 
num_cust = int(input())
dictionary= dict(input().split() for x in range(num_cust))
val = Counter(dictionary).values()
lst = list(val)
for i in range(0, len(lst)):
    lst[i] = int(lst[i])

key = Counter(dictionary).keys()
lst2 = list()
for i in range(0, len(lst2)):
    lst2[i] = int(lst2[i])

Sum = sum(lst) 
print(Sum)

