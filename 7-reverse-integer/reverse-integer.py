class Solution(object):
    def reverse(self, x):
        if x == 0:
            return 0
        while x % 10 == 0:
            x /= 10
        neg = False
        if x < 0:
            neg = True
            x = -x
        res = int(str(x)[::-1])
        if neg:
            res = -res
        if res > 2147483647:
            return 0
        elif res < -2147483648:
            return 0
        return res