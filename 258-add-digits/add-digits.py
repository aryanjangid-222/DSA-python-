class Solution(object):
    def addDigits(self, num):
        if num < 10:
            return num
        while num>9:
            s = 0
            while num != 0:
                s += num%10
                num //= 10
            num =  s
            if num < 10:
                return num
        
        