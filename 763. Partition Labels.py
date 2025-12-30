class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_indexes = defaultdict(int)
        for i, char in enumerate(s):
            last_indexes[char] = i
        
        ans = []
        start = 0
        last_index = 0

        for i, char in enumerate(s):
            last_index = max(last_index, last_indexes[char])
            if last_index == i:
                ans.append(i - start + 1)
                start = i + 1
        
        return ans