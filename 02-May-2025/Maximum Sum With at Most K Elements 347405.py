# Problem: Maximum Sum With at Most K Elements - https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/description/

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        max_hp=[]
        for i in range(len(grid)):
            grid[i].sort(reverse=True)
            for j in range(limits[i]):
                heappush(max_hp, -grid[i][j])
        # print(max_hp)
        ans=0
        for _ in range(k):
            ans+=(-heappop(max_hp))
        # print(ans)
        return ans
