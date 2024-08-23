'''
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
'''

def rotate(nums,k):
    """
    Do not return anything, modify nums in-place instead.
    """
    k = k%len(nums)
    temp = [0] * len(nums)
    for i in range(len(nums)):
        new_position = (i + k) % len(nums)
        temp[new_position] = nums[i]
    nums[:] = temp
    return nums


# Test cases
test_cases = [
    ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
    ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
    ([1, 2, 3, 4, 5], 8, [3, 4, 5, 1, 2])
]

for nums, k, expected in test_cases:
    rotate(nums, k)
    print(f"Input: nums = {nums}, k = {k}")
    print(f"Output: {nums}")
    print(f"Expected: {expected}")
    print(f"Pass: {nums == expected}")
    print()