N = int(input())
Numbers = input().split()

if all(int(i) >= 0 for i in Numbers):
    if any(num == num[-1:] for num in Numbers):
        print("True")
    else:
            print("False")
else:
    print("False")
    
    
