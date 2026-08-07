class Solution(object):
    def hammingDistance(self, x, y):
        n = 0
        a = format(x,'b')
        b = format(y,'b')
        a = "0"*(32-len(a))+a
        b = "0"*(32-len(b))+b
        for i in range(32):
            if a[i]!=b[i]:
                n += 1       
        return n