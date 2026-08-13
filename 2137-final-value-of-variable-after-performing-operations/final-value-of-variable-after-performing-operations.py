class Solution(object):
    def finalValueAfterOperations(self, operations):
        a = 0
        b = 0
        for el in operations:
            if el=="--X" or el=="X--":
                b += 1
            else:
                a += 1
        if a==b:
            return 0
        elif a>b:
            return a-b
        else:
            return -(b-a)