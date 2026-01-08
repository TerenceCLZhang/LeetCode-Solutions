class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations_count = [0] * (n + 1)
        for c in citations:
            if c >= n:
                citations_count[n] += 1
            else:
                citations_count[c] += 1

        papers = 0
        for h in range(n, -1, -1):
            papers += citations_count[h]
            if papers >= h:
                return h
