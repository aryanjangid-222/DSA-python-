class Solution(object):
    def removeDuplicates(self, nums):
        index_value = 1
        for i in range (1,len(nums)):
            if nums[i] != nums[i-1]:
              nums[index_value] = nums [i]
              index_value += 1
        return  index_value