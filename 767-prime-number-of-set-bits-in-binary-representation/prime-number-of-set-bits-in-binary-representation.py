class Solution(object):
    def countPrimeSetBits(self, left, right):
        res = 0
        for i in range(left,right+1):
            a = 0
            while i != 0:
                if i % 2:
                    a += 1
                    i //= 2
                else:
                    i /= 2
            if a in [2,3,5,7,11,13,17,19]:
                res += 1
        return res