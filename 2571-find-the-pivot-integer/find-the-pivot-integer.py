class Solution(object):
    def pivotInteger(self, n):
        s = sum(range(1,n+1))
        rs = 0
        for el in range(1,n+1):
            rs += el
            if rs == s:
                return el
            s -= el
        return -1