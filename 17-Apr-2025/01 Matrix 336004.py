# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        que=deque()
        rows, cols=len(mat), len(mat[0])

        for i in range(rows):
            for j in range(cols):
                if mat[i][j]==0:
                    que.append([i, j])
                else:
                    mat[i][j]=-1
        
        # print(que)
        # print(mat)
        directions=[(-1, 0),(1, 0), (0, -1), (0, 1)]
        def inbound(x, y):
            return 0<=x<rows and 0<=y<cols

        while que:
            r, c=que.popleft()
            for x, y in directions:
                nr, nc=r+x, c+y
                if inbound(nr, nc) and mat[nr][nc]==-1:
                    mat[nr][nc] = mat[r][c] + 1
                    que.append([nr, nc])
        # print(mat)
        return mat
