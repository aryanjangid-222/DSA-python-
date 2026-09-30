class Solution(object):
    def isPossibleToSplit(self, nums):
        li = list(set(nums))
        for el in li:
            if nums.count(el) > 2:
                return False
        
        return True
        