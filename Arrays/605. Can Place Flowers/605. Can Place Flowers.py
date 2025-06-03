class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if n <= 0:
                return True

            prev_empty = (i == 0 or flowerbed[i - 1] == 0)
            curr_empty = (flowerbed[i] == 0)
            next_empty = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)

            if prev_empty and curr_empty and next_empty:
                flowerbed[i] = 1
                n -= 1

        return n <= 0

# Time: O(n)
# Space: O(1)