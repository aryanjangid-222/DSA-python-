class Solution(object):
    def createTargetArray(self, nums, index):
        out = []
        c = -1
        for i in index:
            c += 1
            out.insert(i,nums[c])
        return out