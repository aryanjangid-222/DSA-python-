class Solution(object):
    def generate(self, numRows):
        out = []
        pre = [1]
        for i in range(numRows):
            curr = []
            for j in range(-1,i):
                if j == -1:
                    curr.append(pre[0])
                elif j == i-1:
                    curr.append(pre[len(pre)-1])
                else:
                    curr.append(pre[j] + pre[j+1])
            out.append(curr)
            pre = curr
        
        return out