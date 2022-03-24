#one liner O(n.log(n))
def sortArray(nums):
    nums.sort()
    return nums

#Bubble sort O(n^2)
def sortArray2(nums):
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                temp = nums[j + 1]
                nums[j + 1] = nums[j]
                nums[j] = temp
    return nums


print(sortArray2([1, 7, 2, 4, 1, 88, 45]))