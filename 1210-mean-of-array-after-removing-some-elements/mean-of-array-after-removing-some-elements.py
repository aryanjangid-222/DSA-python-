class Solution(object):
    def trimMean(self, arr):
        arr.sort()
        l = len(arr)
        d = l/20
        sum = 0
        count = 0
        for i in range(d,l-d):
            sum += arr[i]
            count += 1
        count = float(str(count)+".00000")
        return sum/count