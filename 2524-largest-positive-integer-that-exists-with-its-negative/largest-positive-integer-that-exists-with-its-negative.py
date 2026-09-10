class Solution(object):
    def findMaxK(self, nums):
        nums.sort()
        for el in nums:
            if -el in nums:
                return -el 

        return -1