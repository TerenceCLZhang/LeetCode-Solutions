class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        return len(counter.values()) == len(set(counter.values()))

# Time: O(n)
# Space: O(n)