class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = "".join(f"{len(s)}#{s}" for s in strs)
        return encoded_string
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = s.index('#', i)
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res