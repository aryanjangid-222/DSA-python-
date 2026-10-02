class Solution(object):
    def findMinDifference(self, timePoints):
        check = []
        for el in timePoints:
            check.append(int(el[0:2]) * 60 + int(el[3:]))
        
        check.sort()
        l = len(check)
        res = check[1] - check[0]
        for i in range(l-1):
            dif = check[i+1] - check[i]
            if dif < res:
                res = dif
        if 1440-check[l-1] + check[0] < res:
            return  1440-check[l-1] + check[0]
        return res