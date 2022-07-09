nums = list(map(int, input().split()))
li = []
for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i] < nums[j]:
            nums[i] , nums[j] = nums[j] , nums[i]
            
print(nums)
