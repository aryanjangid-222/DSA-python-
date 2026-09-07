class Solution(object):
    def findMiddleIndex(self, nums):
        right = sum(nums) - nums[0]
        left = 0
        l = len(nums)
        for i in range(l-1):
            if left == right:
                return i
            left += nums[i]
            right -= nums[i+1]
        
        return -1 if left != 0 else l-1