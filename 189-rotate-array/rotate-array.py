class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        first = nums[-k:]
        second = nums[:-k]
        nums[:] = first + second
        return nums