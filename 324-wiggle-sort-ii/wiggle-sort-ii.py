class Solution(object):
    def wiggleSort(self, nums):
        nums.sort()
        l = len(nums) + 1
        ist = nums[:l/2][::-1]
        iind = nums[l/2:][::-1]
        for i in range(l - 1):
            if i % 2:
                nums[i] = iind[0]
                iind.remove(iind[0])
            else:
                nums[i] = ist[0]
                ist.remove(ist[0])