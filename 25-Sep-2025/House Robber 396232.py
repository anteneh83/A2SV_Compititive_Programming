# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1 for i in range(len(nums))] 

        def helper(i):
            if i == 0:
                return nums[i]
            if i == 1:
                return max(nums[0], nums[1])
            if memo[i] == -1:
                memo[i] = max(helper(i-1), nums[i] + helper(i-2))
            return memo[i]
        
        return helper(len(nums)-1)  

