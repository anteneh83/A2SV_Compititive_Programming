# Problem: Single Number - https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans=0
        for num in nums:
            ans = ans ^ num
        # print(ans)
        return ans