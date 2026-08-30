class Solution(object):
    def countCommas(self, n):
        return 0 if n < 1000 else n - 999