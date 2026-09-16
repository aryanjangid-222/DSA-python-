class Solution(object):
    def rearrangeArray(self, nums):
        p = 0
        n = 1
        l = len(nums)
        out = [0]*l
        for i in range(l):
            if nums[i] < 0:
                out[n] = nums[i]
                n += 2
            else:
                out[p] = nums[i]
                p += 2
        return out 