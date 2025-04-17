# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        que=deque()
        rows, cols=len(isWater), len(isWater[0])
        for i in range(rows):
            for j in range(cols):
                if isWater[i][j]==1:
                    que.append([i, j])
                    isWater[i][j]=0
                else:
                    isWater[i][j]=-1
        # print(que)
        directions=[(-1, 0),(1, 0), (0, -1), (0, 1)]
        def inbound(x, y):
            return 0<=x<rows and 0<=y<cols

        while que:
            r, c = que.popleft()
            for x, y in directions:
                nr, nc=r+x, c+y
                if inbound(nr, nc) and isWater[nr][nc]==-1:
                    isWater[nr][nc]=isWater[r][c] + 1
                    que.append([nr, nc])
        # print(isWater)
        return isWater

