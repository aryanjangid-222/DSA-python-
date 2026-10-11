class Solution(object):
    def mySqrt(self, x):
        i = 1
        while True:
            if i*i == x:
                return i
            elif i*i > x:
                return i - 1
            i += 1