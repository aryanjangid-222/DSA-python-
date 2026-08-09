class Solution(object):
    def sortArrayByParity(self, nums):
        out1 = []
        out2 = []
        for i in nums:
            if i%2==0:
                out1.append(i)
            else:
                out2.append(i)
        return out1+out2