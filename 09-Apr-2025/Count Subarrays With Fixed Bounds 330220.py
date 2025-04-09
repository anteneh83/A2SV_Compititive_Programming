# Problem: Count Subarrays With Fixed Bounds - https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        max_idx=min_idx=bad_idx=-1
        ans=0
        for i in range(len(nums)):
            if not minK <= nums[i] <= maxK:
                bad_idx=i
            if nums[i]==minK:
                min_idx=i
            if nums[i]==maxK:
                max_idx=i

            ans+=max(0, min(min_idx, max_idx) - bad_idx)            
           
        return ans
        