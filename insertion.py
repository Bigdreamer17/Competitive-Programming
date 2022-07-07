def insertionSort(n , arr):
    key = arr[-1]

    j = n-2
    while j >= 0 and  key < arr[j] :
        arr[j+1] = arr[j]
        print(*arr)
        j -= 1
    arr[j + 1] = key
    print(*arr)
    

n =int(input())
   
arr = list(map(int,input().strip().split()))[:n]

insertionSort(n, arr)


