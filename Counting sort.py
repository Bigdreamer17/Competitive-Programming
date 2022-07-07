def countingSort(arr):
    # Write your code here
    zeros = [0] * n
    for i in arr:
        zeros[i] += 1
    print(*zeros)
    
        

if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))[:n]

    countingSort(arr)

