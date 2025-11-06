# Problem: Solving Questions With Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0]*(n + 1)

        for i in range(n-1, -1, -1):
            points, skip = questions[i]
            take = points
            if i + skip + 1 < n:
                take += dp[i + skip + 1] 
            dp[i] = max(take, dp[i+1])
        # print(dp)
        return dp[0]