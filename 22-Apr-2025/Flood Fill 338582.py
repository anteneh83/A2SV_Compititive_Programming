# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        directions=[(0, 1), (0, -1), (1, 0), (-1, 0)]
        original_color=image[sr][sc]
        if original_color == color:
            return image
        def inbound(p, q):
            return 0<=p<len(image) and 0<=q<len(image[0])
        
        def dfs(original_color, row, col):
            if not inbound(row, col) or original_color != image[row][col]:
                return
            
            image[row][col]=color
            for x, y in directions:
                nr=row+x
                nc=col+y
                dfs(original_color, nr, nc)

            return image

        return dfs(original_color, sr, sc)