class Solution(object):
    def longestSubarray(self, nums):
        l = len(nums)
        if nums.count(1) >= l-1:
            return l-1
        m = 0
        pre = 0
        curr = 0
        for i in range(l-1):
            if nums[i] == 0 and nums[i+1] == 0:
                if m < pre + curr:
                    m = pre + curr
                pre = 0
                curr = 0
            elif nums[i] == 0: 
                if m < curr + pre:
                    m = curr + pre
                pre = curr
                curr = 0
            else:
                curr += 1
        s = pre + curr
        if nums[l-1] == 1:
            return m if m > s + 1 else s + 1
        else:
            return m if m > s else s