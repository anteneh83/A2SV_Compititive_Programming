# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def sub(idx, temp):
            if idx>=len(nums):
                ans.append(temp.copy())
                return
            # leave it
            sub(idx+1, temp)

            # take it
            temp.append(nums[idx])
            sub(idx+1, temp)
            temp.pop()
        sub(0, [])
        return ans