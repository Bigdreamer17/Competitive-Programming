col , ro = map(int, input().split())
row = [input() for i in range(col)]
k = int(input())

for roro in sorted(row, key=lambda roro: int(roro.split()[k])):
    print(roro)
    
    
"""
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1


"""