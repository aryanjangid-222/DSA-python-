class Solution(object):
    def decimalRepresentation(self, n):
        out = []
        i = -1
        while n != 0:
            i += 1
            a = n%10*10**i
            if a != 0:
                out.append(a)
            n = n//10
        return out[::-1]