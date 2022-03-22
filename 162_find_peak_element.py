#Brute force approach O(n)
def findPeakElement(nums) -> int:
    if len(nums) < 2:
        return 0
    else:
        if nums[0] > nums[1]:
            return 0
        elif nums[-1] > nums[-2]:
            return len(nums) - 1
        else:    
            for i in range(len(nums)):
                if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                    return i


#O(Log(n)) sol
def findPeakElement(nums) -> int:
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    
    return left

print(findPeakElement([1,2,1,3,5,6,4]))
#Output: 5