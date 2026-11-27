class Solution(object):
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        ist = abs(bx2-bx1)*abs(by2-by1)
        iind = abs(ax2-ax1)*abs(ay2-ay1)
        y = len(set(range(ay1,ay2)) & set(range(by1,by2)))
        x = len(set(range(ax1,ax2)) & (set(range(bx1,bx2))))

        return (ist + iind) - (x * y) 