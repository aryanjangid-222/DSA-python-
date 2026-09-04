class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        n = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime and endTime[i] >= queryTime:
                n += 1
        return n