class Solution(object):
    def alternateDigitSum(self, n):
        i = 0
        res = 0
        n = int(str(n)[::-1])
        while n != 0:
            if i%2==0:
                res += n%10
                n //= 10
                i += 1
                continue
            else:
                res -= n%10
                n //= 10
                i += 1

        return res
        