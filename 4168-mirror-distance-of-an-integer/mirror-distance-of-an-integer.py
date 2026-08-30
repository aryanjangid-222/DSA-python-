class Solution(object):
    def mirrorDistance(self, n):
        n1 = int(str(n)[::-1])
        return n1 - n if n1 > n else -(n1 - n)