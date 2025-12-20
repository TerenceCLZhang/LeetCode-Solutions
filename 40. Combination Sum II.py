class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        curr = []

        candidates.sort()

        def backtrack(start, summ):
            if summ == target:
                ans.append(curr[:])
                return

            if summ > target:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                curr.append(candidates[i])
                backtrack(i + 1, summ + candidates[i])
                curr.pop()

        backtrack(0, 0)
        return ans
