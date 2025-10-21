# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        idx = len(nums) - 1
        memo = {}

        def fun(idx , curr_sum):
            if (idx, curr_sum) in memo:
                return memo[(idx, curr_sum)]
            if idx < 0 and curr_sum == target:
                return 1
            if idx < 0:
                return 0

            positive = fun(idx - 1, curr_sum + nums[idx])
            negative = fun(idx - 1, curr_sum + -nums[idx])

            memo[(idx, curr_sum)] = positive + negative

            return memo[(idx, curr_sum)]
        
        return fun(idx, 0)