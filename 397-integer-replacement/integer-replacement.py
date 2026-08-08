class Solution(object):
    def integerReplacement(self, n):
        a = 0
        l = n
        if n>100:
            l = 50
        for i in range(l):
            if n==1:
                return a
            if n%2==0:
                n = n/2
                a += 1
            else:
                if n==3:
                    n += 1
                elif n%4==1:
                    n -= 1
                    a += 1
                else:
                    n += 1
                    a += 1
        return a

        