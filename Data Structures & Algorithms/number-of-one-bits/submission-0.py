class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= (n-1) #remove lowest 1 bit, flips the rightmost n to 0
            count +=1
        return count