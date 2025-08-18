# Problem: D - Restricted Permutation - https://codeforces.com/gym/607625/problem/D

from collections import defaultdict
import heapq
n, m =map(int, input().split())
graph = defaultdict(list)
in_degree = [0]*n
for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    in_degree[b-1] +=1
# print(graph)
# print(in_degree)
min_heap = [i+1 for i in range(n) if in_degree[i]==0]
heapq.heapify(min_heap)
# print(min_heap)
ans=[]

while min_heap:
    top= heapq.heappop(min_heap)
    ans.append(top)
    for nei in graph[top-1]:
        in_degree[nei]-=1
        if in_degree[nei]==0:
            heapq.heappush(min_heap, nei+1)
# print(ans)
if len(ans) == n:
    print(*ans)
else:
    print(-1)