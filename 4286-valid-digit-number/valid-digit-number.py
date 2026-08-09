class Solution(object):
    def validDigit(self, n, x):
        n = str(n)
        x = str(x)
        if n.count(x)<1:
            return False
        else:
            if n[0]==x:
                return False
        return True

        