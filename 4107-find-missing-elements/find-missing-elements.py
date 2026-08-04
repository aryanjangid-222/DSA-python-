class Solution(object):
    def findMissingElements(self, nums):
        nums.sort()
        out = []
        a = len(nums)
        if nums[a-1]-nums[0]+1==a:
            return out
        for i in range(a-1):
            if nums[i]!=nums[i+1]-1:
                b =  nums[i+1]-nums[i]
                for j in range(1,b):
                    out.append(nums[i]+j)
        return out
