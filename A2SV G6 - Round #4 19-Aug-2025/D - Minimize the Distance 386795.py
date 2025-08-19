# Problem: D - Minimize the Distance - https://codeforces.com/gym/590053/problem/D

n=int(input())
nums=list(map(int, input().split()))
nums.sort()
ans=n//2

if n%2 == 0:
    print(nums[ans-1])
else:
    print(nums[ans])