from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        num_citations = [0] * (n + 1)

        for c in citations:
            num_citations[min(c, n)] += 1

        papers = 0
        for h in range(n, -1, -1):
            papers += num_citations[h]
            if papers >= h:
                return h
