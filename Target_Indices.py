num= sorted((list(map(int, input().split()))))
target = int(input())
li = []
count = 0
for i in range(len(num)):
    if num[i] == target:
        count += 1
        li.append(count)
print(li)
