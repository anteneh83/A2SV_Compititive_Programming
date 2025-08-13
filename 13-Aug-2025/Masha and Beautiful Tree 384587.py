# Problem: Masha and Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

import sys
sys.setrecursionlimit(10**6)

def solve_case(nums):
    n = len(nums)
    
    def dfs(arr):
        if len(arr) == 1:
            return arr, 0  
        
        mid = len(arr) // 2
        left, l_ops = dfs(arr[:mid])
        right, r_ops = dfs(arr[mid:])
        
        if left is None or right is None:
            return None, -1  
        
        if left[-1] <= right[0]:
            return left + right, l_ops + r_ops
    
        if right[-1] <= left[0]:
            return right + left, l_ops + r_ops + 1
        
        return None, -1
    
    _, res = dfs(nums)
    return res

t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    print(solve_case(nums))
