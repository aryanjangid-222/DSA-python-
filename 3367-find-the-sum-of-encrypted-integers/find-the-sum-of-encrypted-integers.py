class Solution(object):
    def sumOfEncryptedInt(self, nums):
        s = 0
        for el in nums:
            if el < 10:
                s += el
                continue
            el = str(el)
            l = len(el)
            m = 0
            for i in el:
                if int(i)>m:
                    m = int(i)
            n = str(m)*l
            s += int(n)
        return s

        