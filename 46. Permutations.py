class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curr = []

        def backtrack():
            if len(curr) == len(nums):
                ans.append(curr[:])
                return

            for i in range(len(nums)):
                if nums[i] not in curr:
                    curr.append(nums[i])
                    backtrack()
                    curr.pop()

        backtrack()
        return ans
