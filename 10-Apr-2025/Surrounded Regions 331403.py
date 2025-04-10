# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions=[(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols=len(board), len(board[0])
        
        def dfs(row, col):
            if (row < 0 or row >= rows) or ( col < 0 or col >= cols) or board[row][col] !='O':
                return 

            board[row][col]='E'
            for x, y in directions:
                dfs(row+x, col+y)

        for i in range(rows):
            if board[i][0]=='O':
                dfs(i, 0)
            if board[i][cols - 1]=='O':
                dfs(i, cols-1)
        
        
        for j in range(cols):
            if board[0][j]=='O':
                dfs(0, j)
            if board[rows-1][j]=='O':
                dfs(rows-1, j)

        for i in range(rows):
            for j in range(cols):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]=='E':
                    board[i][j]='O'

        # print(board)
        return board