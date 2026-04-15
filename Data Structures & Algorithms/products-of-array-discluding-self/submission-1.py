class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            left_p = math.prod(nums[:i])
            right_p = math.prod(nums[i+1:])
            product = left_p * right_p
            output.append(product)
        return output
