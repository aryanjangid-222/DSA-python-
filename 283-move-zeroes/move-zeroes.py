class Solution(object):
    def moveZeroes(self, nums):
        write = 0
        for read in range(len(nums)):
            if nums[read]!=0:
                tmp = nums[write]
                nums[write]=nums[read]
                nums[read]=tmp
                write += 1