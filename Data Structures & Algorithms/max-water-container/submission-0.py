class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        best = 0
        for height in heights:
            distance = r - l
            maximum = min(heights[l], heights[r]) * distance
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            best = max(best, maximum)
        return best