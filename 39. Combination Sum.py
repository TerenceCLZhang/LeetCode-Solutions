class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        curr = []

        def backtrack(summ):
            if summ == target:
                ans.append(curr[:])
                return

            if summ > target:
                return

            for c in candidates:
                curr.append(c)
                backtrack(summ + c)
                curr.pop()

        backtrack(0)
        return ans
