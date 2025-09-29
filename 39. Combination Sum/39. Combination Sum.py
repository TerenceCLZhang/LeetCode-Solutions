from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ans, curr = [], []

        def backtrack(start, curr_sum):
            if curr_sum == target:
                ans.append(curr[:])
                return

            if curr_sum > target:
                return

            for i in range(start, n):
                curr.append(candidates[i])
                backtrack(i, curr_sum + candidates[i])
                curr.pop()

        backtrack(0, 0)
        return ans
