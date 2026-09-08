class Solution(object):
    def average(self, salary):
        n = (len(salary)-2)*1.00000
        s = sum(salary) - min(salary) - max(salary)
        return s/n
        