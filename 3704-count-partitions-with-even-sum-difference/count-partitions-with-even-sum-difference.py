class Solution(object):
    def countPartitions(self, nums):
        n = 0
        for i in range(1,len(nums)):
            if (sum(nums[0:i]) - sum(nums[i:])) % 2 == 0:
                n += 1
        
        return n