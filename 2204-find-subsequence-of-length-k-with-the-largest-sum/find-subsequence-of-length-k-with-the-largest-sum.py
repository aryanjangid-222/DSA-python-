class Solution(object):
    def maxSubsequence(self, nums, k):
        l = len(nums)
        for i in range(l-k):
            nums.remove(min(nums))
        return nums
    
