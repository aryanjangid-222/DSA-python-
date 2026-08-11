class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        sorted_nums = sorted(nums)
        
        lookup = {}
        for idx, num in enumerate(sorted_nums):
            if num not in lookup:
                lookup[num] = idx
        return [lookup[num] for num in nums]
               
        
