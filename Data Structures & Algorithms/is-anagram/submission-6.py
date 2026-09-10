from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        counts = defaultdict(int)
        for char in s:
            counts[char] += 1
        for char in t:
            counts[char] -= 1
        for char in counts:
            if counts[char] != 0:
                return False
        return True
        
        