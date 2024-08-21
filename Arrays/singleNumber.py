'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
'''


def singleNumber(nums) :
    # d = {}
    # for i in nums:
    #     if i not in d:
    #         d[i] = 1
    #     else: 
    #         d[i] += 1
    # for k,v in d.items() :
    #     if v == 1:
    #         return k
    res=0
    for i in nums:
        res=res^i
    return res

nums = [2,2,1]
print(singleNumber(nums))  #ouput : 1
