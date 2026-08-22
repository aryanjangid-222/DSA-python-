class Solution(object):
    def isHappy(self, n):
        c = 0
        while True:
            c += 1
            if c==9:
                return False
            if n==1:
                return True
            a = str(n)
            n = 0
            for el in a:
                n += int(el)**2
            if n == 1:
                return True