class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        d = arr[1] - arr[0]
        l = len(arr)
        for i in range(1,l):
            if arr[i] - arr[i-1] != d:
                return False
        return True