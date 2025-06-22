class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []
        i = 0

        while i < len(s):
            chunk = s[i:i + k]
            if len(chunk) < k:
                chunk += fill * (k - len(chunk))
            ans.append(chunk)
            i += k

        return ans

# Time: O(n)
# Space: O(1)
