# check whether the given array is sorted and rotated. 
def check(nums):
    count = 0
    n = len(nums)

    for i in range(n):
        if nums[i] > nums[(i + 1) % n]:   # if the current element is greater then its next element , it means rotated
            count += 1
            if count > 1:
                return False

    return True

# testcases: 

nums1 = [3,4,5,1,2]
nums2 = [2,1,3,4]
nums3 = [1,1,1]

print(check(nums1))
print("----------------")

print(check(nums2))
print("----------------")

print(check(nums3))
print("----------------")