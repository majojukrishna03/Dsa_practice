'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
'''
def missingNumber(nums):
    n = len(nums)
    expected_sum = (n*(n+1))//2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# Test Case 1: Missing number in the middle
nums1 = [3, 0, 1]
print(missingNumber(nums1))  # Expected Output: 2

# Test Case 2: Missing number at the end
nums2 = [0, 1]
print(missingNumber(nums2))  # Expected Output: 2

# Test Case 3: Larger array with a missing number
nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(missingNumber(nums3))  # Expected Output: 8