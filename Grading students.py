import math

grades_count = int(input().strip())

grades = []  
for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)
        
for i in range(len(grades)):
    multiple = math.ceil(grades[i] / 5) * 5
    result = multiple - grades[i]
    
    if  result < 3 and grades[i] >= 38:
        grades[i] = multiple
    if result >= 3:
        grades[i] = grades[i]

for i in grades:
    print(i)
