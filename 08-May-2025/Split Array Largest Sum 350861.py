# Problem: Split Array Largest Sum - https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        left, right = max(nums), sum(nums)
        ans = right

        def helper(max_sum):
            sub_count=1
            curr_sum=0

            for num in nums:
                if curr_sum + num > max_sum:
                    sub_count+=1
                    curr_sum = num
                else:
                    curr_sum+=num
            return sub_count <= k

        while left <= right:
            mid =(left + right)//2
            if helper(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        # print(ans)
        return  ans

