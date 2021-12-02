def binsearch(nums, start, end, target):
    if start > end: 
        return False
    mid = (start + end) // 2 
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binsearch(nums, mid+1, end, target)
    else:
        return binsearch(nums, start, mid -1 , target)
    
nums = [1,2,3,4,5,6,7,8,9,10]
print(binsearch(nums, 0, len(nums)-1, 4))
        