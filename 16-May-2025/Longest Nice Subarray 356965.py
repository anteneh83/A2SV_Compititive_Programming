# Problem: Longest Nice Subarray - https://leetcode.com/problems/longest-nice-subarray/

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l=0
        ans=0
        curr=0
        for r in range(len(nums)):
            while curr & nums[r]:
                curr ^= nums[l]
                l+=1
            curr |= nums[r]
            
            ans = max(ans, r - l + 1)
        # print(ans)
        return ans
            

           