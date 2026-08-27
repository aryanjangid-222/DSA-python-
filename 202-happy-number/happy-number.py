class Solution(object):
    def isHappy(self, n):
        check = []
        while n!=1:
            check.append(n)
            s = 0
            while n!=0:
                s += (n%10)**2
                n = n//10
            n = s
            if n in check:
                return False
        return True