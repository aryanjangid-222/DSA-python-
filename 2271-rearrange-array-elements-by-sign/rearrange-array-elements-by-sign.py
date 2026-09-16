class Solution(object):
    def rearrangeArray(self, nums):
        pos = []
        neg = []
        out = []
        for el in nums:
            if el > 0:
                pos.append(el)
            else:
                neg.append(el)
        for i in range(len(neg)):
            out.append(pos[i])
            out.append(neg[i])
            
        return out