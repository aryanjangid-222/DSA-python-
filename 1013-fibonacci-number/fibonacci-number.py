class Solution(object):
    def fib(self, n):
        totalSum = 0
        next = 0
        first = 1
        second = 0
        for i in range(1,n+1):
            totalSum += first
            next = first + second
            first = second
            second = next
        return totalSum