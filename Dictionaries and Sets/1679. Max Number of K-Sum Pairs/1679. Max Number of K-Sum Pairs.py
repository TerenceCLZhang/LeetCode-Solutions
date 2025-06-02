class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        c = defaultdict(int)
        ops = 0

        for n in nums:
            compliment = k - n
            if c[compliment] > 0:
                c[compliment] -= 1
                ops += 1
            else:
                c[n] += 1
        
        return ops

# Time: O(n)
# Space: O(n)
