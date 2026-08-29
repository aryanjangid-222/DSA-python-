class Solution(object):
    def productExceptSelf(self, nums):
        out = []
        pro = 1
        a = 0
        for el in nums:
            if el != 0:
                pro *= el
            else:
                a += 1
        if a == 1:
            for el in nums:
                if el != 0:
                    out.append(0)
                else:
                    out.append(pro)
        elif a > 1:
            for el in nums:
                out.append(0)
        else:
            for el in nums:
                out.append(pro/el)
        return out