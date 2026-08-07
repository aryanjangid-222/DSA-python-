class Solution(object):
    def reverseBits(self, n):
        a = format(n,'b')[::-1]
        a = a+"0"*(32-len(a))
        return int(a,2)
        
        