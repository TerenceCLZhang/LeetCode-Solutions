from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans, curr = [], []
        used = [False] * n

        def backtrack():
            if len(curr) == n:
                ans.append(curr[:])
                return

            for i in range(n):
                if not used[i]:
                    used[i] = True
                    curr.append(nums[i])
                    backtrack()
                    curr.pop()
                    used[i] = False

        backtrack()
        return ans
