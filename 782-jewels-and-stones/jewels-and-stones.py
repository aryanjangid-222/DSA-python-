class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        a = 0
        for el in jewels:
            b = stones.count(el)
            if b > 0:
                a += b
        return a
        