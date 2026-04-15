class Solution:
    def rob(self, nums: List[int]) -> int:
        x = len(nums)
        if x == 1:
            return nums[0]
        def dfs(i, end, memo):
            if i > end:
                return 0
            if i in memo:
                return memo[i]
            memo[i] = max(
                nums[i] + dfs(i + 2, end, memo), dfs(i + 1, end, memo)
                ) 
            return memo[i]
        return max(
            dfs(0, x - 2, {}), # exclude last
            dfs(1, x - 1, {}) # exclude first
        )