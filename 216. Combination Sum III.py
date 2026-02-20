class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        curr = []

        def backtrack(start):
            if len(curr) == k:
                if sum(curr) == n:
                    ans.append(curr[:])
                return

            for i in range(start, 10):
                curr.append(i)
                backtrack(i + 1)
                curr.pop()

        backtrack(1)
        return ans
