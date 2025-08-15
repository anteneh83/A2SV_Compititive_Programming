# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n=len(board)
        def get_cord(sq, n):
            row= (n-1) - (sq-1)//n
            col=(sq-1)%n

            if (n-row)%2==0:
                col=(n-1) - col
            return row, col
        
        que=deque([[1, 0]])#start square and step
        visited=set()

        while que:
            sq, move=que.popleft()
            for i in range(1, 7):
                new_sq=sq + i
                if new_sq > n*n:
                    continue
                r, c= get_cord(new_sq, n)

                if board[r][c] != -1:
                    new_sq=board[r][c]
                if new_sq==n*n:
                    return move+1
                if new_sq not in visited:
                    visited.add(new_sq)
                    que.append([new_sq, move+1])
        return -1
