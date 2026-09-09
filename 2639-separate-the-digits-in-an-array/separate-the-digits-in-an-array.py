class Solution(object):
    def separateDigits(self, nums):
        out = []
        for el in nums:
            for i in str(el):
                out.append(int(i))
        
        return out