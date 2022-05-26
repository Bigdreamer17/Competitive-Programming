n = int(input())
lst = []

for _ in range(n+1):
    lst.append(_)
for j in lst:
    if lst[j] % 3 == 0 and lst[j] % 5 == 0:
        lst[j] = 'FizzBuzz'
    elif lst[j] % 3 == 0:
          lst[j] = 'Fizz'
    elif lst[j] % 5 == 0:
          lst[j] = 'Buzz'  
    else:
        lst[j] = lst[j]
print(lst[1: ])
