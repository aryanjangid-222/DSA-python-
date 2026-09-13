class Solution(object):
    def smallestIndex(self, nums):
        for i in range(len(nums)):
            el = nums[i]
            if el == i and el < 10:
                return i
            if el > 9:
                s = 0
                while el != 0:
                    s += el % 10
                    el //= 10
                
                if s == i:
                    return i
        
        return -1
            