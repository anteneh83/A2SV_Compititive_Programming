# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        rev_graph=defaultdict(list)
        out_degree=[0]*len(graph)

        for u in range(len(graph)):
            out_degree[u]=len(graph[u])
            for v in graph[u]:
                rev_graph[v].append(u)
        # print(rev_graph)
        # print(out_degree)
        queue = deque([i for i in range(len(graph)) if out_degree[i] == 0])
        safe = [False] * len(graph)

        while queue:
            node = queue.popleft()
            safe[node] = True
            for prev in rev_graph[node]:
                out_degree[prev] -= 1
                if out_degree[prev] == 0:
                    queue.append(prev)

        return [i for i in range(len(graph)) if safe[i]]