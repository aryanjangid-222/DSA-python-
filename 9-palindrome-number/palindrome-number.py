class Solution(object):
    def isPalindrome(self, x):
        rev = 0
        org = x
        while x>0:
            rev = rev*10 + x%10
            x = x//10
        return rev==org