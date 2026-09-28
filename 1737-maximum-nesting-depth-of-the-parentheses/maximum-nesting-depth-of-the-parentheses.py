class Solution(object):
    def maxDepth(self, s):
        a = 0
        max_1 = 0
        for i in s:
            if i=="(":
                a += 1
                if max_1<a:
                    max_1=a
            elif i==")":
                a -= 1
        return max_1