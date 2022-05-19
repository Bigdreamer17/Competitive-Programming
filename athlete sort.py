col , ro = map(int, input().split())
row = [input() for i in range(col)]
k = int(input())

for roro in sorted(row, key=lambda roro: int(roro.split()[k])):
    print(roro)
    
