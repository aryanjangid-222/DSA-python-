class Solution(object):
    def targetIndices(self, nums, target):
        out = []
        nums.sort()
        for i in range(len(nums)):
            if out != []:
                if nums[i] == target:
                    out.append(i)
                else:
                    return out
            elif nums[i] == target:
                out.append(i)

        return out    
            