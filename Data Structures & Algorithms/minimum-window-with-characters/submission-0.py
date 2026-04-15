class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)
        my_len = 0
        best_len = float('inf')
        l = 0
        for r in range(len(s)):
            window = s[l: r+1]
            if need[s[r]] > 0:
                missing -= 1
            need[s[r]] -= 1 # in case need[s[r]] > 1
            while missing == 0:
                if r - l + 1 < best_len:
                    my_len = l
                    best_len = r - l + 1
                need[s[l]] += 1
                if need[s[l]] > 0:
                    missing += 1
                l += 1
        if best_len == float('inf'):
            return ""
        return s[my_len: my_len + best_len]           
               

            
            
    
