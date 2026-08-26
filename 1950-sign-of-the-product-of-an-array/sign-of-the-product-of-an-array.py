class Solution(object):
    def arraySign(self, nums):
        if 0 in nums:
            return 0
        a = 1
        for el in nums:
            if el<0:
                a *= -1
        return 1 if a==1 else -1