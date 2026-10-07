class Solution(object):
    def sortArray(self, arr):
        
        n = len(arr)

        size = 1
        while size < n:
            left = 0
            while left < n - 1:
                mid = left + size - 1
                right = min(left + 2 * size - 1, n - 1)
        
                if mid < right:
                    temp = []
                    i, j = left, mid + 1
            
                    while i<= mid and j <= right:
                        if arr[i] <= arr[j]:
                            temp.append(arr[i])
                            i += 1
                        else:
                            temp.append(arr[j])
                            j += 1
                    
                    while i <= mid:
                        temp.append(arr[i])
                        i += 1
                    while j <= right:
                        temp.append(arr[j])
                        j += 1
                
                    for k in range(len(temp)):
                        arr[left + k] = temp[k]
                
                left += 2 * size
            size *= 2
        return arr