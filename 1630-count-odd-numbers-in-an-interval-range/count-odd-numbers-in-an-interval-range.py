class Solution(object):
    def countOdds(self, low, high):
            return (high - low) / 2 if (low % 2 == 0 and high % 2 == 0) else (high - low) // 2 + 1 