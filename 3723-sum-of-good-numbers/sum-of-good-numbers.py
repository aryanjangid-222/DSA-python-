class Solution(object):
    def sumOfGoodNumbers(self, nums, k):
        l = len(nums)
        s = 0
        for i in range(l):
            el = nums[i]
            neg = i - k
            pos = i + k
            if neg < 0:
                if nums[i] > nums[pos]:
                    s += el
                    continue
                neg = i
            if pos > l-1:
                if nums[i] > nums[neg]:
                    s += el
                    continue
                pos = i
            if el > nums[neg] and el > nums[pos]:
                s += el
        
        return s