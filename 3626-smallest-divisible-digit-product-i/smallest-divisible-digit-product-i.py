class Solution(object):
    def smallestNumber(self, n, t):
        for i in range(n,n+t+1):
            a = 1
            c = i
            while c>0:
                a *= c%10
                c /=10
            if a%t==0:
                return i
        return n