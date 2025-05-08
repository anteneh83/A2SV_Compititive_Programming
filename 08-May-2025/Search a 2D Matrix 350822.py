# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # rows = len(matrix)

        for r in matrix:
            row = set(r)
            if target in row:
                return True
        return False