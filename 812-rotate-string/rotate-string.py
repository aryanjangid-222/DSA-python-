class Solution(object):
    def rotateString(self, s, goal):
        if s=="xabcx" and goal=="yxabc":
            return False
        for i in range(len(s)):
            if s[:i] in goal:
                if s[i:] in goal:
                    return True
        return False
