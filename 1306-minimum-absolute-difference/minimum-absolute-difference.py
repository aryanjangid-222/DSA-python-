class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        out = []
        a = 10000000
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]<=a:
                out.append([arr[i],arr[i+1]])
                a = arr[i+1]-arr[i]
        res = []
        for el in out:
            if el[1]-el[0]==a:
                res.append(el)
        return res
        