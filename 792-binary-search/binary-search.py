class Solution(object):
    def search(self, nums, target):
        l = len(nums)
        left = 0
        right = l-1
        if target == nums[left]:
            return left
        elif target == nums[right]:
            return right
        while left < right:
            mid = (left + right)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid-1
        if nums[left] == target:
            return left
        return -1