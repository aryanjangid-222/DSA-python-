class Solution(object):
    def smallestRepunitDivByK(self, k):
        if k % 2 == 0 or k % 5 == 0:
            return -1
        num = 0
        i = 0
        while True:
            i += 1
            num = num*10 + 1
            if num % k == 0:
                return i
        
        return -1