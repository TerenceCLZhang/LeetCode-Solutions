class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst():
            l = 0
            r = len(nums) - 1
            index = -1

            while l <= r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1

                if nums[m] == target:
                    index = m

            return index

        def findLast():
            l = 0
            r = len(nums) - 1
            index = -1

            while l <= r:
                m = (l + r) // 2
                if nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1

                if nums[m] == target:
                    index = m

            return index

        return [findFirst(), findLast()]

# Time: O(log n)
# Space: O(1)
