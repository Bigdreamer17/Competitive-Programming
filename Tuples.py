number_list = []
size =  int(input("size of tuple: "))
item = list(map(int, input().split()))
if len(item) > size:
    print("No!!!!!!!!!!")
for i in range(0, size):
    number_list.append(item)
    
t = tuple(item)
print(hash(t))