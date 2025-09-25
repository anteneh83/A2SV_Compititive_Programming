# Problem: Longest Common Subsequence - https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # memo = {}
        # def dp(i, j):
        #     if (i, j) in memo:
        #         return memo[(i,j)]
        #     if i >= len(text1) or j >= len(text2):
        #         return 0
        #     max_val = 0

        #     if text1[i] == text2[j]:
        #         max_val = 1 + dp(i+1, j+1)
        #     else:
        #         max_val = max(dp(i+1, j), dp(i, j+1))
        #     memo[(i, j)] = max_val

        #     return memo[(i, j)]
        # return dp(0, 0)

        # bottom up
        n, m = len(text1), len(text2)

        dp = [[0]*(m+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        # print(dp)
        return dp[n][m]
            
