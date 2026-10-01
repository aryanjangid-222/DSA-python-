class Solution(object):
    def topKFrequent(self, nums, k):
        check = {}
        li = list(set(nums))
        for el in li:
            check[el] = 0
        for el in nums:
            check[el] += 1 
        return sorted(check, key=check.get, reverse=True)[:k]
        
        