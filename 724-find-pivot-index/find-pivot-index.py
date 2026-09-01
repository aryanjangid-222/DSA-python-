class Solution(object):
    def pivotIndex(self, nums):
        s = 0
        s1 = 0
        for el in nums:
            s += el
        i = -1
        for el in nums:
            i += 1
            s -= el
            if s1==s:
                return i
            s1 += el
        return -1
        