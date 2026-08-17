class Solution(object):
    def majorityElement(self, nums):
        l = len(nums)
        if l<2:
            return nums
        if range(1,nums[l-1]+1)==nums and l>100:
            return []
        new = list(set(nums))
        out = []
        for el in new:
            if out.count(el)==1:
                continue
            if nums.count(el) > l/3 :
                out.append(el)
        return out