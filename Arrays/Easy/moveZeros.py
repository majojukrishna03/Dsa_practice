'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
'''

def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    i = 0
    j = 0
    while(j < len(nums)):
        if nums[j] != 0: 
            nums[i],nums[j] = nums[j], nums[i]
            i+=1
        j+=1
    return nums

# Test cases
test_cases = [
    ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
    ([0, 0, 1], [1, 0, 0]),
    ([1, 2, 3, 4], [1, 2, 3, 4])
]

for nums, expected in test_cases:
    moveZeroes(nums)
    print(f"Input: {nums}")
    print(f"Output: {nums}")
    print(f"Expected: {expected}")
    print(f"Pass: {nums == expected}")
    print()