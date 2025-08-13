# Problem: Skibidus and Fanum Tax (hard version) - http://codeforces.com/problemset/problem/2065/C2

import bisect

def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        b.sort()
        prev = -float('inf')
        possible = True
        for num in a:
            no_op = num
            target = prev + num
            idx = bisect.bisect_left(b, target)
            if idx < m:
                op_val = b[idx] - num
            else:
                op_val = None
            choices = []
            if no_op >= prev:
                choices.append(no_op)
            if op_val is not None and op_val >= prev:
                choices.append(op_val)
            if not choices:
                possible = False
                break
            prev = min(choices)
        print("YES" if possible else "NO")

solve()