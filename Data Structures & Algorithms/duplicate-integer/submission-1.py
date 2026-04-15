class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        no_dups = set(nums)
        if len(nums) == len(no_dups):
            return False
        return True