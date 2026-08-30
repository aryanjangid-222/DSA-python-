class Solution(object):
    def removeZeros(self, n):
        res = ""
        for el in str(n):
            if int(el) != 0:
                res += el
        return int(res)