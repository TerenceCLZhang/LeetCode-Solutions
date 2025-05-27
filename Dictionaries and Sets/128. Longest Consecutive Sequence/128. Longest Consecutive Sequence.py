class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        longest = 0

        for n in sett:
            if n - 1 not in sett:
                curr = n
                curr_length = 1
                while curr + 1 in sett:
                    curr += 1
                    curr_length += 1

                longest = max(longest, curr_length)

        return longest 

# Time: O(n)
# Space: O(n)