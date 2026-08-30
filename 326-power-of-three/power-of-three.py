class Solution(object):
    def isPowerOfThree(self, n):
        if n<3:
            return n==1
        while n != 1:
            if n%3 == 0:
                n = n/3
            else:
                return False
        else:
            return True