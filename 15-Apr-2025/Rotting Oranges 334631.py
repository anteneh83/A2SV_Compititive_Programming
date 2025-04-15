# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions=[(1, 0), (-1, 0), (0, 1), (0, -1)]

        def inbound(x, y):
            return 0<=x<len(grid) and 0<=y<len(grid[0])
        
        dq=deque()
        oneCount=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    dq.append([i, j])
                elif grid[i][j]==1:
                    oneCount+=1
        if oneCount==0:
            return oneCount
        minute=0
        while dq:
            minute+=1
            for i in range(len(dq)):
                row, col = dq.popleft()

                for x, y in directions:
                    nr, nc=row+x, col+y
                    if inbound(nr, nc) and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        oneCount-=1
                        dq.append([nr, nc])
        # print(grid)

        return minute-1 if oneCount==0 else -1