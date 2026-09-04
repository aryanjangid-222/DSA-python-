class Solution(object):
    def threeConsecutiveOdds(self, arr):
        n = 0
        for el in arr:
            if el % 2 != 0:
                n += 1
            else:
                n = 0
            if n == 3:
                return True
        return False