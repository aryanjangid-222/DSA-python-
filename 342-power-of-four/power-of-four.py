class Solution(object):
    def isPowerOfFour(self, n):
        if n < 0:
            return False
        a = format(n,'b')
        if len(a)<32:
            a = "0"*(32-len(a))+a
        if a.count('1')==1 and a.find('1')%2!=0:
            return True
        else:
            return False
        