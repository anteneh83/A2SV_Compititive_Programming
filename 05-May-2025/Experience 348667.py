# Problem: Experience - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/C

n, m = map(int, input().split())

parent = list(range(n + 1))
rank = [0] * (n + 1)
add = [0] * (n + 1)
diff = [0] * (n + 1)

def find(x):
    if parent[x] != x:
        par = parent[x]
        parent[x] = find(par)
        diff[x] += diff[par]
    return parent[x]

def get(x):
    find(x)
    return diff[x] + add[find(x)] 

def union(x, y):
    rx, ry = find(x), find(y)
    if rx == ry:
        return
    if rank[rx] < rank[ry]:
        parent[rx] = ry
        diff[rx] = add[rx] - add[ry]
    else:
        parent[ry] = rx
        diff[ry] = add[ry] - add[rx]
        if rank[rx] == rank[ry]:
            rank[rx] += 1

for _ in range(m):
    parts = input().split()
    if parts[0] == "join":
        x, y = int(parts[1]), int(parts[2])
        union(x, y)
    elif parts[0] == "add":
        x, exp = int(parts[1]), int(parts[2])
        add[find(x)] += exp
    else:  
        x = int(parts[1])
        print(get(x))
