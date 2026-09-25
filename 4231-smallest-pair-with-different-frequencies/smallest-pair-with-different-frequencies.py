class Solution(object):
    def minDistinctFreqPair(self, nums):
        nums.sort()
        num = nums[0]
        f = nums.count(num)
        for el in nums:
            if f != nums.count(el):
                return [num,el]
        return [-1,-1]