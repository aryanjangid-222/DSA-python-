class Solution(object):
    def maxArea(self, height):
        res = 0
        left = 0
        right = len(height) - 1
        while left < right:
            wid = right - left
            area = wid * min(height[left],height[right])
            if res < area:
                res = area
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        
        return res