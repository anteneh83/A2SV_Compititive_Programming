# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions=[(0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (1, 1), (-1, -1), (1, -1)]
        rows, cols=len(board), len(board[0])
        def inbound(x, y):
            return 0 <= x < rows and 0 <= y < cols

        def mines_counter(r, c):
            mines_count=0
            for x, y in directions:
                nr, nc=r+x, c+y
                if inbound(nr, nc) and board[nr][nc]=='M':
                    mines_count+=1
            return mines_count
        r, c=click
        if board[r][c]=='M':
            board[r][c]='X'
            return board
        que=deque([(r, c)])
        visited=set((r, c))
        while que:
            r, c = que.popleft()
            mines=mines_counter(r, c)
            if mines > 0:
                board[r][c]=str(mines)
            else:
                board[r][c]='B'
                for x, y in directions:
                    nr, nc=r+x, c+y
                    if inbound(nr, nc) and (nr, nc) not in visited:
                        if board[nr][nc]=='E':
                            que.append((nr, nc))
                            visited.add((nr, nc))
        return board

