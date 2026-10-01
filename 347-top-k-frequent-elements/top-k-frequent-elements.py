class Solution(object):
    def topKFrequent(self, nums, k):
        check = {}
        li = list(set(nums))
        for el in li:
            check[el] = nums.count(el)
        sorted_keys = sorted(check, key=check.get)
        l = len(sorted_keys)
        return sorted_keys[l-k:]
        
        