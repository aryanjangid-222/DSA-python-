class Solution(object):
    def smallestIndex(self, nums):
        for i,el in enumerate(nums):
            if i == el and el < 10:
                return i
            else:
                s = 0
                while el != 0:
                    s += el % 10
                    el //= 10
                if i == s:
                    return i
            
        return -1