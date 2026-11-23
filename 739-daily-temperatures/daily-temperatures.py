class Solution(object):
    def dailyTemperatures(self, temp):
        l = len(temp)
        res = [0] * l
        check = [l-1]
        for j in range(l-1,-1,-1):
            if temp[j] >= temp[check[0]]:
                check = [j]
                continue
            else:
                left = -1
                while temp[check[-1]] <= temp[j]:
                    left -= 1
                    check.pop()
                check.append(j)
                for el in check[::-1]:
                    if temp[j] < temp[el]:
                        res[j] = el-j
                        break
        
        return res