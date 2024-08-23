'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
'''

def removeDuplicates(nums):
        if not nums: 
            return 0

        k = 1

        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        return k

# testcases: 

nums1 = [1,1,2]
nums2 = [0,0,1,1,1,2,2,3,3,4]

print("nums1")
print(removeDuplicates(nums1))
print()

print("nums2")
print(removeDuplicates(nums2))
print()
