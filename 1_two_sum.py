'''Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]'''

class Solution:
    #O(N^2)
    '''def twoSum(nums,target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return i,j'''

    #O(N)           
    def twoSum(nums, target):
        nums_dict = {}
        for i in range(len(nums)):
            nums_dict[nums[i]] = i

        print(nums_dict)

        for i in range(len(nums)):
            bal = target - nums[i]
            print(f"balance: {bal} at i: {i}")
            if bal in nums_dict and  nums_dict[bal] != i:
                return i, nums_dict[bal]




# nums = [2,7,11,15]
# target = 9


nums = [3,2,4]
target = 6


# nums = [3,3]
# target = 6
print(Solution.twoSum(nums,target))
                


