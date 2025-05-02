# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        parent = {i: i for i in range(n+1)}
        size={i: 1 for i in range(n+1)}

        def find(x):
            root=x
            stk=[]
            while parent[root] != root:
                stk.append(parent[root])
                root=parent[root]
            while stk:
                parent[stk.pop()]=root
            return root
        
        def union(x, y):
            root_x=find(x)
            root_y=find(y)

            if root_x != root_y:
                if size[root_x] < size[root_y]:
                    parent[root_x] = root_y
                    size[root_y] += size[root_x]
                else:
                    parent[root_y] = root_x
                    size[root_x] += size[root_y]
                return False
            else:
                return True

        ans=[]
        for x, y in edges:
            if union(x, y) :
                ans.append([x, y])
        return ans[-1]  