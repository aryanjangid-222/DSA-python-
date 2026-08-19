class Solution(object):
    def longestConsecutive(self, nums):
        if len(nums)<2:
            return len(nums)
        a = 0
        nums = list(set(nums))
        nums.sort()
        l = len(nums)
        out = 1
        max = 0
        for i in range(l-1):
            if nums[i]==nums[i+1]-1:
                out += 1
            elif max<out:
                max = out
                out = 1
            else:
                out = 1
        if out>max:
            return out
        return max