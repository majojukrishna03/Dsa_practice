'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''
def twoSum( nums,target):
    a = {}
    for i,num in enumerate(nums):
        b = target - num
        if b in a:
            return [i,a[b]]
        a[num] = i

# test cases :

print(twoSum(nums=[2,7,11,15],target=9)) # Output: [0,1] || [1,0]
print(twoSum(nums=[3,2,4],target=6)) # Output: [1,2] || [2,1]
print(twoSum(nums=[3,3],target=6)) # Output: [0,1] || [1,0]
