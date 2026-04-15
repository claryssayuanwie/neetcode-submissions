class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # using two ptr technique, sorting is needed bc 
        # left > increaases sum, right < decreases sum
        result = []
        nums.sort()
        
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            target = -nums[i]

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while j < k:
                need = nums[j] + nums[k]

                if need == target:
                    triplet = [nums[i], nums[j], nums[k]]
                    result.append(triplet)
                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                
                elif need < target:
                    j += 1
                else:
                    k -= 1

        return result

            # result = [triplet]

