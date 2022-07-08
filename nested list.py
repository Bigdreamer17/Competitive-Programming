Number_students = int(input("Enter number of students: "))

student_mark = []
for i in range(0,Number_students):
    student_mark.append([input("Enter student name: "), float(input("Enter student mark: "))])

new_sublist = sorted(list(set([marks for name, marks in student_mark])))[1]

print('\n'.join([a for a,b in sorted(student_mark) if b == new_sublist]))

   
