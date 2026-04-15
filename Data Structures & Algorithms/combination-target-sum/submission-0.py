class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(r, start, path, result):
            if r < 0:
                return 
            if r == 0:
                result.append(list(path))
                return
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(r - nums[i], i, path, result)
                path.pop()

        result = []
        backtrack(target, 0, [], result)
        return result