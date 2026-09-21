class Solution(object):
    def tribonacci(self, n):
        if n == 0:
            return 0
        p2 = 0
        p1 = 1
        p0 = 1
        for i in range(3,n+1):
            c = p2+p1+p0
            p0,p1,p2 = c,p0,p1
        
        return p0    