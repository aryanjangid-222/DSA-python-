class Solution(object):
    def subtractProductAndSum(self, n):
        n = str(n)
        s = 0
        p = 1
        for i in n:
            s += int(i)
            p *= int(i)
        return p-s
        