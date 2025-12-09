class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []

        for l, h in intervals:
            if not merged or merged[-1][1] < l:
                merged.append([l, h])
            else:
                merged[-1][1] = max(merged[-1][1], h)

        return merged
