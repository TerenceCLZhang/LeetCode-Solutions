class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit))
        cache = {}

        def dfs(i):
            if i in cache:
                return cache[i]

            if i == len(intervals):
                return 0

            # don't include element
            res = dfs(i + 1)

            # include element
            j = self.binarySearch(intervals, i + 1)

            res = max(res, intervals[i][2] + dfs(j))
            cache[i] = res
            return res

        return dfs(0)

    def binarySearch(self, intervals, start):
        target_end = intervals[start - 1][1]

        left = start
        # will return an invalid index if no more available
        right = len(intervals)

        while left < right:
            mid = (left + right) // 2
            if intervals[mid][0] < target_end:
                left = mid + 1
            else:
                right = mid

        return left
