class Solution(object):
    def finalValueAfterOperations(self, operations):
        x = 0
        for i in operations:
            if i[1]=='-':
                x=x-1
            else:
                x=x+1
        return x