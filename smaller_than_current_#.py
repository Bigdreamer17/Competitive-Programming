num = list(map(int, input().split()))
count = 0
count_list = []
for i in range(len(num)):
    for j in range(len(num)):
        if i != j and num[j] < num[i] and num[j] != num[i]:
            count += 1
    count_list.append(count)
    count = 0
print(count_list)



