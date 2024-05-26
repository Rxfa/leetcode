class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_h = 0
        while left < right:
            curr_h = min(height[left], height[right]) * (right - left)
            max_h = max(max_h, curr_h)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_h
