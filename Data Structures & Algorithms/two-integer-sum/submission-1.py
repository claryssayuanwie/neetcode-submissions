class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # find indices i and j s.t. their values add to target
        # complement + num[i] = target
        # complement = target - num[i]
        seen = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in seen:
                return [seen[complement], i]
            seen[n] = i # set seen num to index
            
