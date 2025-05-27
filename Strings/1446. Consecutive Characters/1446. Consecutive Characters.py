class Solution:
    def maxPower(self, s: str) -> int:
        max_power = 1
        curr_power = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr_power += 1
            else:
                max_power = max(max_power, curr_power)
                curr_power = 1

        return max(max_power, curr_power)

# Time: O(n)
# Space: O(1)