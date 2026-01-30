class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        n = len(s)
        res = []
        increment = 2 * (numRows - 1)

        for r in range(numRows):
            for i in range(r, n, increment):
                res.append(s[i])
                if 0 < r < numRows - 1 and i + increment - 2 * r < n:
                    res.append(s[i + increment - 2 * r])

        return "".join(res)
