class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text1)
        cols = len(text2)
        memo = [[None] * (cols + 1) for i in range((rows + 1))]

        for row in range(rows + 1):
            for col in range(cols + 1):
                if row == 0 or col == 0:
                    memo[row][col] = 0
                elif text1[row - 1] == text2[col - 1]:
                    memo[row][col] = memo[row - 1][col - 1] + 1
                else:
                    memo[row][col] = max(memo[row - 1][col], memo[row][col - 1])
        return memo[rows][cols]
