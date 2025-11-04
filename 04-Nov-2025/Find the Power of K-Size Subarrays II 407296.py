# Problem: Find the Power of K-Size Subarrays II - https://leetcode.com/problems/find-the-power-of-k-size-subarrays-ii/

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # if k == 1:
        #     return nums  
        # inc = [0]*(n-1)


        # for i in range(n-1):
        #     if nums[i+1] == (nums[i] + 1):
        #         inc[i] = 1

        # res = []
        # count = sum(inc[:k-1])

        # for i in range(n-k +1):
        #     if i > 0:
        #         count -= inc[i-1]
        #         count+= inc[i+k - 2]
        #     if count == k - 1:
        #         res.append(nums[i + k - 1])
        #     else:
        #         res.append(-1)

        # return res

        prev = count =0
        res = []

        for val in nums:
            if val - prev ==1:
                count +=1
            else:
                count = 1
            if count >= k:
                res.append(val)
            else:
                res.append(-1)
            prev = val
        return res[k-1:]