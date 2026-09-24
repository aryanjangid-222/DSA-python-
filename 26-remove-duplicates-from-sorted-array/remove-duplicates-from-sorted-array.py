class Solution(object):
    def removeDuplicates(self, nums):
        check = list(set(nums))
        check.sort()
        l = len(check)
        for i in range(l):
            nums[i] = check[i]
        
        return l