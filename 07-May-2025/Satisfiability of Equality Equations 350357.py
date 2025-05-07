# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        n=len(equations)
        parent = [i for i in range(26)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  
            return parent[x]
        
        def union(x, y):
            root_x=find(x)
            root_y=find(y)

            if root_x != root_y:
                parent[root_y] = root_x
                 
        
        for var in equations:
            x = ord(var[0]) - ord('a')
            y = ord(var[3]) - ord('a')
            if var[1] == '=':
                union(x, y)
            
        for var in equations:
            x = ord(var[0]) - ord('a')
            y = ord(var[3]) - ord('a')
            if var[1]=='!':
                if find(x) == find(y):
                    return False
        return True
