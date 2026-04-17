class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0 # best next range we can reach after one more jump
        jumps = 0 # jumps taken
        end = 0 # how far we can go with current jumps
        for i in range(len(nums) - 1): # loop through an array. do not take another step at last index.
            farthest = max(farthest, i + nums[i])
            #if we explored everything in curr range
            if i == end: 
                jumps += 1
                end = farthest
        return jumps


                