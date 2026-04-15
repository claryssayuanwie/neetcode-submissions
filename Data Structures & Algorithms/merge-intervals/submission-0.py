class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        for start, end in intervals:
            if len(res) == 0:
                res.append([start, end])
            else:
                last_start, last_end = res[-1]
                if start <= last_end:
                    #overlap -> merge
                    res[-1][1] = max(last_end, end)
                else:
                    res.append([start, end])
        return res