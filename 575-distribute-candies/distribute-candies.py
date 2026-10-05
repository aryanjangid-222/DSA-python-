class Solution(object):
    def distributeCandies(self, candyType):
        mid = len(candyType)/2
        check = list(set(candyType))
        return len(check) if len(check) < mid else mid
