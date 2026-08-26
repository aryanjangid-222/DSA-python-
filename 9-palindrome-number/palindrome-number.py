class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        x1 = x[::-1]
        return x==x1
        