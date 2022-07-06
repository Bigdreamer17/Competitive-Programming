M , N = map(int, input().split())
if N % 2 == 0:
    max_dom = N/2 + M 
elif M % 2 != 0 and N % 2 != 0:
    max_dom = (M * N)/2    
print(int(max_dom))