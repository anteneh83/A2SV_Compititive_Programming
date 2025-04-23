# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        
        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1 / val))

        # print(graph)
        ans=[-1.0]*len(queries)
        for i in range(len(queries)):
            start, end= queries[i]
            if start not in graph:
                ans[i]=-1.0
                continue
            que=deque([(start, 1.0)])
            visited=set([start])
            found=False
            while que:
                node, curr_val=que.popleft()
                if node == end:
                    ans[i]=curr_val
                    found=True
                    break
                for var, val in graph[node]:
                    if var not in visited:
                        visited.add(var)
                        que.append((var, curr_val*val))
            if not found:
                ans[i]=-1.0
        return ans