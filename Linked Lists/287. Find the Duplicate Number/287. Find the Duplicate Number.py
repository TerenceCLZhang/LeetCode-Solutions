class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = 0

        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]

            if fast == slow:
                break

        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

# Time: O(n)
# Space: O(1)
