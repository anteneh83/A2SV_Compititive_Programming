# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        
        heap = [(0, 0)]
        totalCost = 0
        visited= set()

        while len(visited) < n:
            cost, u = heappop(heap)
            if u in visited:
                continue

            visited.add(u)
            totalCost += cost

            for v in range(n):
                if v not in visited:
                    cost = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    heappush(heap, (cost, v))

        # print(totalCost)
        return totalCost



