# Problem: Possible Bipartition - https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        colors=[-1]*n
        adjucency_list=[[] for _ in range(n)]
        for u, v in dislikes:
            adjucency_list[u-1].append(v-1)
            adjucency_list[v-1].append(u-1)
        # print(adjucency_list)
        
        def dfs(node, adjucency_list):
            for nei in adjucency_list[node]:
                if colors[nei]==-1:
                    colors[nei]= 1 - colors[node]
                    if not dfs(nei, adjucency_list):
                        return False
                elif colors[nei]==colors[node]:
                    return False
            return True

        for node in range(n):
            if colors[node]==-1:
                colors[node]=0
                if not dfs(node, adjucency_list):
                    return False

        return True
