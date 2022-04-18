array_list = []

n = int(input("Number of elements: "))

for i in range (0, n):
    inputlist = [int(input("input list: "))]
    array_list.append(inputlist)

array_list.sort(reverse = True)
print(array_list)
print("The Runner-up is: ", array_list[1])
