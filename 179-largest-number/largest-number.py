class Solution(object):
    def largestNumber(self, nums):
        while True:
            isnotchange = True
            for i in range(1,len(nums)):
                num1 = int(str(nums[i-1]) + str(nums[i]))
                num2 = int(str(nums[i]) + str(nums[i-1]))
                if num2 > num1:
                    nums[i],nums[i-1] = nums[i-1],nums[i]
                    isnotchange = False
            if isnotchange:
                break
        
        return str(int("".join(map(str,nums))))