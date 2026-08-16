class Solution(object):
    def consecutiveSetBits(self, n):
        s = format(n,'b')
        if s.count("11")==1:
            if s.count("111")==1:
                return False
            return True
        else:
            return False