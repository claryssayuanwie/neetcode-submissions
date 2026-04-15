class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0
        for num in seen:
            if num - 1 not in seen: # smallest num
                seq = 1
                curr = num
                
                while curr + 1 in seen: # while num + 1 exists in set
                    seq += 1
                    curr += 1
                longest = max(seq, longest)
            
        return longest


        
