class Solution(object):
    def countOdds(self, low, high):
        x = high - low
        if low % 2 == 0 and high % 2 == 0:
            return x / 2
        else:
            return x // 2 + 1