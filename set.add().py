lis = []
stamp_num = int(input("Enter the number of stamps: "))
for i in range(stamp_num):
    stamp_name = input("Enter country names: ")
    lis.append(stamp_name)
s = set(lis)
print("The number of stamps is: " , len(s))