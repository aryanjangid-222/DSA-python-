class Solution(object):
    def reverseVowels(self, s):
        s = list(s)
        left = 0
        right = len(s) - 1
        check = ['a','e','i','o','u','A','E','I','O','U']
        while left < right:
            if s[left] in check:
                if s[right] in check:
                    s[left],s[right] = s[right],s[left]
                    left += 1
                    right -= 1
                else:
                    right -= 1
            else:
                left += 1
        return "".join(s)