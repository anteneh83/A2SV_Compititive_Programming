# Problem: Minimum Operations to Exceed Threshold Value II - https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        hp=[]
        for num in nums:
            heappush(hp, num)
        # print(hp)
        operation=0
        while hp[0] < k:
            num1=heappop(hp)
            num2=heappop(hp)
            add=min(num1, num2)*2 + max(num1, num2)
            heappush(hp, add)
            operation+=1
        return operation