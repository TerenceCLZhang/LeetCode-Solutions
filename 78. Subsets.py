class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        curr = []

        def backtrack(start):
            ans.append(curr[:])

            for i in range(start, n):
                curr.append(nums[i])
                backtrack(i + 1)
                curr.pop()

        backtrack(0)
        return ans
