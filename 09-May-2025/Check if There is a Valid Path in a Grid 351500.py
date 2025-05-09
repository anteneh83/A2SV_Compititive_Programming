# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) 
        return self.parent[x]
    
    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)


class Solution:
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])
        uf = UnionFind(m * n)

        directions = {
            1: [(0, -1), (0, 1)],       # left, right
            2: [(-1, 0), (1, 0)],       # up, down
            3: [(0, -1), (1, 0)],       # left, down
            4: [(0, 1), (1, 0)],        # right, down
            5: [(0, -1), (-1, 0)],      # left, up
            6: [(0, 1), (-1, 0)],       # right, up
        }

        opposite = {
            (0, -1): (0, 1),
            (0, 1): (0, -1),
            (-1, 0): (1, 0),
            (1, 0): (-1, 0),
        }

        def in_bounds(x, y):
            return 0 <= x < m and 0 <= y < n

        for i in range(m):
            for j in range(n):
                curr_type = grid[i][j]
                for dx, dy in directions[curr_type]:
                    ni, nj = i + dx, j + dy
                    if in_bounds(ni, nj):
                        nei = grid[ni][nj]
                        if opposite[(dx, dy)] in directions[nei]:
                            curr_idx = i * n + j
                            next_idx = ni * n + nj
                            uf.union(curr_idx, next_idx)

        return uf.find(0) == uf.find(m * n - 1)
