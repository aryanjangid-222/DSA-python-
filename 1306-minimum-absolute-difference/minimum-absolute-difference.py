class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        l = len(arr)
        out = []
        a = 2*arr[l-1]
        for i in range(l-1):
            if arr[i+1]-arr[i]<=a:
                out.append([arr[i],arr[i+1]])
                a = arr[i+1]-arr[i]
        res = []
        for el in out:
            if el[1]-el[0]==a:
                res.append(el)
        return res
        