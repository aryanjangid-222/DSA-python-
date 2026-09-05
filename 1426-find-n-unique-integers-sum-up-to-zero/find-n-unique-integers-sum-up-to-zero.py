class Solution(object):
    def sumZero(self, n):
        if n%2 != 0:
            h = n//2
            return range(-h,h+1)
        else:
            h = n/2
            out = range(-h,h+1)
            out.remove(0)
            return out

