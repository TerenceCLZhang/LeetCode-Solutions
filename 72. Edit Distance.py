class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0 and len(word2) == 0:
            return 0

        dp = [[0] * (len(word1) + 1) for _ in range(len(word2) + 1)]

        for i in range(len(word2)):
            dp[i][-1] = len(word2) - i

        for j in range(len(word1)):
            dp[-1][j] = len(word1) - j

        for i in range(len(word2) - 1, -1, -1):
            for j in range(len(word1) - 1, -1, -1):
                if word1[j] == word2[i]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = min(dp[i + 1][j + 1], dp[i]
                                   [j + 1], dp[i + 1][j]) + 1

        print(dp)

        return dp[0][0]
