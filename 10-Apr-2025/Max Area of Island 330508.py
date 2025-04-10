# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions=[(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols=len(grid), len(grid[0])
        def inbound(r, c):
            return 0 <= r <rows and 0 <= c< cols
        
        def dfs(visited, row, col):
            # base case 
            if not inbound(row, col) or (row, col) in visited or grid[row][col]==0:
                return 0
            visited.add((row, col))
            area=1
            for x, y in directions:
                area += dfs(visited, row+x, col+y)
            return area
        
        visited=set()
        ans=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1 and (i, j) not in visited:
                    ans= max(ans, dfs(visited, i, j))
        return ans

