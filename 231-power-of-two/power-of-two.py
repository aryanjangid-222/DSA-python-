class Solution(object):
    def isPowerOfTwo(self, n):
        if n < 0:
            return False
        a = format(n,'b')
        if a.count("1")==1:
            return True
        else:
            return False
        