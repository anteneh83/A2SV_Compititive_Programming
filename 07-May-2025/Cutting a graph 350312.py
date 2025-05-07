# Problem: Cutting a graph - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/D

n, m, k = map(int, input().split())

edges = []
for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))

operations = []
cutting_edges = set()

for _ in range(k):
    parts = input().split()
    op, u, v = parts[0], int(parts[1]), int(parts[2])
    operations.append((op, u, v))
    if op == "cut":
        cutting_edges.add((u, v))
        cutting_edges.add((v, u))  

parent = {i: i for i in range(1, n + 1)}
size = {i: 1 for i in range(1, n + 1)}

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
        if size[root_x] < size[root_y]:
            root_x, root_y = root_y, root_x
        parent[root_y] = root_x
        size[root_x] += size[root_y]

for u, v in edges:
    if (u, v) not in cutting_edges:
        union(u, v)


answers = []
for op, u, v in reversed(operations):
    if op == "ask":
        answers.append("YES" if find(u) == find(v) else "NO")
    elif op == "cut":
        union(u, v)

for ans in reversed(answers):
    print(ans)
