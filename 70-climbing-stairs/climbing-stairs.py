class Solution(object):
    def climbStairs(self, n):
        if n<4:
            return n
        f = 3
        s = 2
        c = 0
        for i in range(3,n):
            c = f + s
            s = f
            f = c
        return c



