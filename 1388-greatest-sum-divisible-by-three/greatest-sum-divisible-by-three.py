class Solution(object):
    def maxSumDivThree(self, nums):
        nums.sort()
        a1 = 10000
        a2 = 10000
        a3 = 10000
        a4 = 10000
        for el in nums:
            if a1 != 10000 and a2 != 10000 and a3 != 10000 and a4 != 10000:
                break
            if el % 3 == 1 and a2 == 10000:
                if a1 == 10000:
                    a1 = el 
                    continue
                elif a2 == 10000:
                    a2 = el
            elif el % 3 == 2 and a4 == 10000:
                if a3 == 10000:
                    a3 = el
                elif a4 == 10000:
                    a4 = el
        res = sum(nums)
        if res % 3 == 0:
            return res
        elif res % 3 == 2:
            if a3 != 0:
                if a1 != 10000 and a2 != 10000 and (a1 + a2) < a3:
                    return res - (a1 + a2)
                return res - a3
            else:
                if a1 != 10000 and a2 != 10000:
                    return res - (a1 + a2)
                return 0
        elif a3 + a4 < a1 and a4 != 10000:
                return res - (a3 + a4)
        elif a1 != 10000:
            return res - a1 
        else:
            return 0
