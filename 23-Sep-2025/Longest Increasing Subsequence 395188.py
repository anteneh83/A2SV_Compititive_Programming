# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [-1]*len(nums)

        def dp(idx):
            if memo[idx] != -1:
                return memo[idx]
            max_val = 0
            for j in range(idx+1, len(nums)):
                if nums[j] > nums[idx]:
                    max_val = max(dp(j), max_val)
            memo[idx] = max_val + 1
            return memo[idx]

            
        
        max_len = 0
        for i in range(len(nums)):
            max_len = max(dp(i), max_len)
        return max_len