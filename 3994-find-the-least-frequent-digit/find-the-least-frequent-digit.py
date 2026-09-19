class Solution(object):
    def getLeastFrequentDigit(self, n):
        check = []
        while n != 0:
            check.append(n%10)
            n //= 10
        li = list(set(check))
        li.sort()
        res = check[0]
        f = len(check)
        for el in li:
            c = check.count(el)
            if c < f:
                f = c
                res = el
        
        return res