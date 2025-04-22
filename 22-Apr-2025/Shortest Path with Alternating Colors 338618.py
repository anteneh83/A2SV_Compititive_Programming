# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph=[[] for _ in range(n)]
        R=1
        B=2
        for a, b in redEdges:
            graph[a].append((b, R))
        for x, y in blueEdges:
            graph[x].append((y, B))
        # print(graph)   
        dist_ans=[-1]*n
        que=deque([(0, 0)])
        count=0
        while que:
            for _ in range(len(que)):
                u, prev_color=que.popleft()
                if dist_ans[u]==-1:
                    dist_ans[u]=count
                for i, (v, color) in enumerate(graph[u]):
                    if color == prev_color or v==-1:
                        continue
                    que.append((v, color))
                    graph[u][i]=(-1, color)
            count+=1
        return dist_ans       
        