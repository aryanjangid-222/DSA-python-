class Solution(object):
    def smallestNumber(self, n, t):
        for i in range(n,n+t+1):
            pro = 1
            cur = i
            while cur>0:
                pro *= cur%10
                cur /=10
            if pro%t==0:
                return i
        return n