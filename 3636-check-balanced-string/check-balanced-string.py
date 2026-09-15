class Solution(object):
    def isBalanced(self, num):
        s1 = 0
        s2 = 0 
        for i in range(len(num)):
            if i%2:
                s2 += int(num[i])
                continue
            s1 += int(num[i])
        
        return s1 == s2
        