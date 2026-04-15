class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]: # left > right. min @ index 0 of r
                left = mid + 1
            else:
                right = mid
        return nums[left] # loop ends when left == right, so u return nums[l]


