class Solution(object):
    def shuffle(self, nums, n):
        out = []
        for i in range(n):
            out.append(nums[i])
            out.append(nums[i+n])
        
        return out