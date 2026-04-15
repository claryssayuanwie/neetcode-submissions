class Solution:
    import string
    def characterReplacement(self, s: str, k: int) -> int:
        # given: str s and int k
        # goal: replace some letter x 
        # s.t. substring will contain a distinct letter
        best = 0
        l = 0
        freq = defaultdict(int)
        maxfreq = 0

        for r in range(len(s)):
            freq[s[r]] += 1
            maxfreq = max(maxfreq, freq[s[r]])
            window = r - l + 1
            replacements_n = window - maxfreq
            if replacements_n > k:
                freq[s[l]] -= 1
                l += 1
            best = max(best, r - l + 1)
        return best


        