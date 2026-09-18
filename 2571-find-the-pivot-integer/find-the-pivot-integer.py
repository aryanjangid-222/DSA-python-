class Solution(object):
    def pivotInteger(self, n):
        check = range(1,n+1)
        s = sum(check)
        rs = 0
        for el in check:
            rs += el
            if rs == s:
                return el
            s -= el
        return -1