class Solution(object):
    def hammingWeight(self, n):
        a = format(n,'b')
        return a.count('1')
        