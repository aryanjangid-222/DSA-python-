class Solution(object):
    def scoreOfString(self, s):
        check = [ord(char) for char in s]
        s = 0
        for i in range(len(check)-1):
            s += abs(check[i] - check[i+1])
        
        return s