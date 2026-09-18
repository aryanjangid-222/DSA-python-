class Solution(object):
    def sumOfMultiples(self, n):
        s = 0
        for el in range(1,n+1):
            if el%3==0 or el%5==0 or el%7==0:
                s += el
        
        return s