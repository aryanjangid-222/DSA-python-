class Solution(object):
    def duplicateZeros(self, arr):
        i = -1
        while i < len(arr)-1:
            i += 1
            if arr[i] == 0:
                arr.insert(i,0)
                arr.pop()
                i += 1