class Solution(object):
    def countKDifference(self, nums, k):
        l = len(nums)
        n = 0
        for i in range(l-1):
            for j in range(i+1,l):
                if k == abs(nums[i] - nums[j]):
                    n += 1
        
        return n
