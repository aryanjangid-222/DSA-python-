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
        
        p = 0
        n = 0
        for i in range(len(nums)):
            if p == n:
                out.append(pos[i-p])
                n += 1
            else:
                out.append(neg[i-n])
                p += 1
        
        return out