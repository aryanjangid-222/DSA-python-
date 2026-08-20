class Solution(object):
    def removeElement(self, nums, val):
        index_value = 0
        for i in range (0,len(nums)):
            if nums[i] != val:
              nums[index_value] = nums [i]
              index_value += 1
        return  index_value
            