n =int(input())
   
a = list(map(int,input().strip().split()))[:n]

# Python program for implementation of Bubble Sort

def bubbleSort(a):
  c = 0

  # Traverse through all array elements
  for i in range(n):

    # Last i elements are already in place
    for j in range(0, n-i-1):

      # traverse the array from 0 to n-i-1
      # Swap if the element found is greater
      # than the next element
      if a[j] > a[j+1]:
        a[j], a[j+1] = a[j+1], a[j]
        c += 1

  print("\nArray is sorted in ",c, "swaps")


bubbleSort(a)

print("First element: ",a[0])
print("Last element: ",a[-1])
