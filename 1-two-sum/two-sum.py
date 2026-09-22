class Solution(object):
    def twoSum(self, nums, target):
        seen = {}

        for i, el in enumerate(nums):
            diff = target - el
            
            if diff in seen:
                return [seen[diff], i]
            
            seen[el] = i