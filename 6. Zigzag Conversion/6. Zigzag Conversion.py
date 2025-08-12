class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [[] for _ in range(numRows)]
        pos = 0
        d_pos = 1

        for c in s:
            rows[pos].append(c)

            if pos == numRows - 1:
                d_pos = -1
            elif pos == 0:
                d_pos = 1

            pos += d_pos

        for i in range(numRows):
            rows[i] = "".join(rows[i])

        return "".join(rows)
