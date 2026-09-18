class Solution(object):
    def sumOfMultiples(self, n):
        check = range(1,n+1)
        s = 0
        for el in check:
            if el % 3 == 0:
                s += el
                continue
            elif el % 5 == 0:
                s += el
                continue
            elif el % 7 == 0:
                s += el

        return s
        
        