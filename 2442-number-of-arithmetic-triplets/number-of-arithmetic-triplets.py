class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        n = 0
        for i in range(len(nums)):
            if (nums[i] + diff) in nums[i+1:]:
                if (nums[i] + 2*diff) in nums[i+2:]:
                    n += 1
        return n