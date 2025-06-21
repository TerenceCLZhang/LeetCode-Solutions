class Solution:
    def average(self, salary: List[int]) -> float:
        minn = min(salary)
        maxx = max(salary)
        summ = sum(salary) - minn - maxx
        return summ / (len(salary) - 2)

# Time: O(n)
# Space: O(1)