class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        buckets = [0] * (len(nums) + 1)

        for n, count in counter.items():
            if buckets[count] == 0:
                buckets[count] = [n]
            else:
                buckets[count].append(n)

        ans = []
        for i in range(len(nums), -1, -1):
            if buckets[i] != 0:
                ans += buckets[i]
            if len(ans) == k:
                return ans

# Time: O(n)
# Space: O(n)
