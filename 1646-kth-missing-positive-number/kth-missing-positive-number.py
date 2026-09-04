class Solution(object):
    def findKthPositive(self, arr, k):
        l = len(arr)
        m = arr[l-1]
        check = range(1,m+k+1)
        for el in arr:
            check.remove(el)
        return check[k-1]