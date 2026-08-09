class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()
        l = len(nums)
        if nums[0]<0 and nums[1]<0 and nums[l-1]<0:
            return (nums[l-1]*nums[l-2]*nums[l-3])
        elif nums[0]<0 and nums[1]<0:
            if nums[0]*nums[1]*nums[l-1]>nums[l-1]*nums[l-2]*nums[l-3]:
                return nums[0]*nums[1]*nums[l-1]
        return nums[l-1]*nums[l-2]*nums[l-3]
        
        