class Solution(object):
    def countNegatives(self, grid):
        n = 0
        for el in grid:
            for i in el:
                if i < 0:
                    n += 1
        
        return n