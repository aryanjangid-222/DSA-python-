class Solution(object):
    def wiggleSort(self, nums):
        nums.sort()
        l = len(nums) + 1
        ist = nums[:l/2][::-1]
        iind = nums[l/2:][::-1]
        nums[::2] = ist
        nums[1::2] = iind