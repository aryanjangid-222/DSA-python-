class Solution(object):
    def countDigits(self, num):
        n = 0
        for el in str(num):
            if num%int(el) == 0:
                n += 1
    
        return n