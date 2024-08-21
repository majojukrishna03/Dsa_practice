'''
Given a binary array nums, return the maximum number of consecutive 1's in the array.
'''

def findMaxConsecutiveOnes(nums):
    max_count = 0
    current_count = 0
    
    for num in nums:
        if num == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
    
    return max_count

# test case: 

nums = [1,1,0,1,1,1]
nums1 = [0,1,1,0,0,1]

print(findMaxConsecutiveOnes(nums))
print(findMaxConsecutiveOnes(nums1))