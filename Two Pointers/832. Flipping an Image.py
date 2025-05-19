class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            l = 0
            r = len(row) - 1

            while l <= r:
                if row[l] == row[r]:
                    row[l] = row[r] = 1 - row[l]
                else:
                    row[l], row[r] = row[r], row[l]
                    row[l] = 1 - row[l]
                    row[r] = 1 - row[r]

                l += 1
                r -= 1

        return image

# Time: O(n^2)
# Space: O(1)