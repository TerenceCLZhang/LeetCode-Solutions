class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        arr = [0] * (len(nums) + 1)
        
        for num, freq in counter.items():
            if arr[freq] == 0:
                arr[freq] = [num]
            else:
                arr[freq].append(num)
        
        ans = []
        for i in range(len(nums), 0, -1):
            if arr[i] != 0:
                ans += arr[i]
            if len(ans) >= k:
                break
        
        return ans

# Time: O(n)
# Space: O(n)