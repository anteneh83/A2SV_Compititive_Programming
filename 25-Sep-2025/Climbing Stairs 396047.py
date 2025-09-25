# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
  def climbStairs(self, n: int) -> int:
    # prev1 = 1  # dp[i - 1]
    # prev2 = 1  # dp[i - 2]

    # for _ in range(2, n + 1):
    #   dp = prev1 + prev2
    #   prev2 = prev1
    #   prev1 = dp

    # return prev1
    
    # top down approach
    # memo = {1:1, 2:2}

    # def helper(x):
    #     if x in memo: 
    #         return memo[x]
    #     else:
    #         memo[x] = helper(x-1) + helper(x-2)
    #         return memo[x]
    # return helper(n)

    # bottom up

    if n<=1: return 1
    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]


