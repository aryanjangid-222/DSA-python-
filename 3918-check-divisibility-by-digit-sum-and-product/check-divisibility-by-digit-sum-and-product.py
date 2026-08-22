class Solution(object):
    def checkDivisibility(self, n):
        sum = 0
        pro = 1
        for el in str(n):
            sum += int(el)
            pro *= int(el)
        return n%(sum+pro)==0