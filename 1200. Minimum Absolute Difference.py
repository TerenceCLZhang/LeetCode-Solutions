class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_abs_diff = float("inf")
        ans = []

        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            if diff < min_abs_diff:
                min_abs_diff = diff
                ans = [[arr[i - 1], arr[i]]]
            elif diff == min_abs_diff:
                ans.append([arr[i - 1], arr[i]])
        
        return ans