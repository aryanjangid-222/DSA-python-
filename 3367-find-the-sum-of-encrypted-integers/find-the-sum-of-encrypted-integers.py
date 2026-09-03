class Solution(object):
    def sumOfEncryptedInt(self, nums):
        s = 0
        for el in nums:
            if el < 10:
                s += el
                continue
            l = len(str(el))
            m = 0
            while el != 0:
                n = el % 10
                if n > m:
                    m = n
                el = el//10
            s += int(str(m)*l)
        return s