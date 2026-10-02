class Solution(object):
    def reverse(self, x):
        if x > 0:
            isneg = False
        elif x < 0:
            isneg = True
            x = -x
        else:
            return 0
        while x % 10 == 0:
            x /= 10
        res = 0
        while x != 0:
            res = res*10 + x%10
            x //= 10
        if isneg and res > 2147483648:
            return 0
        elif isneg:
            return -res
        elif res > 2147483647:
            return 0
        return res