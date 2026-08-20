class Solution(object):
    def totalMoney(self, n):
        res = 0
        c = 1
        m = -1
        for i in range(1,n+1):
            if i%7==1:
                m += 1
                c = m
            c += 1
            res += c
        return res