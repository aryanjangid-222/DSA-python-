class Solution(object):
    def checkGoodInteger(self, n):
        s = 0
        p = 0
        while n != 0:
            s += n%10
            p += (n%10)**2
            n //= 10
        
        return (p-s) >= 50