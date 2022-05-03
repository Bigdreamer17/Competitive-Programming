size_of_set1 = int(input("Enter the size of set1: "))
English = list(map(int, input("Enter the number of students: ").split()))
if len(English) > size_of_set1:
    print("out of range!!!")
size_of_set2 = int(input("Enter the size of set2: "))
French = list(map(int, input("Enter the number of students: ").split()))
if len(French) > size_of_set2:
    print("out of range!!!")
set1 = set(English)
set2 = set(French)
uni = set1.union(set2)
print(len(uni))