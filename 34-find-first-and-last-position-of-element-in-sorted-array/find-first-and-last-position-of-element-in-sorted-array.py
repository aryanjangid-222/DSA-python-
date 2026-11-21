class Solution(object):
    def searchRange(self, nums, target):
        def lower_bound(arr ,aim):
            lo,hi = 0,len(arr)
            while lo < hi:
                mid = (lo + hi)//2
                if arr[mid] < aim:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        def upper_bound(arr ,aim):
            lo,hi = 0,len(arr)
            while lo < hi:
                mid = (lo + hi)//2
                if arr[mid] <= aim:
                    lo = mid + 1
                else:
                    hi = mid
            return lo
        
        lb = lower_bound(nums ,target)
        if lb == len(nums) or nums[lb] != target:
            return [-1 ,-1]
        return [lb ,upper_bound(nums ,target)-1]