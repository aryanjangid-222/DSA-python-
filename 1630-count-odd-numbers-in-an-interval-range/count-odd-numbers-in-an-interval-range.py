class Solution(object):
    def countOdds(self, low, high):
        l = low % 2
        h = high % 2
        if l == 0 and h == 0:
            return (high - low) / 2
        else:
            return (high - low) // 2 + 1