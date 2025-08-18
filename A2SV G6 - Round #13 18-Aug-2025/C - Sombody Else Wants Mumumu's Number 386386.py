# Problem: C - Sombody Else Wants Mumumu's Number - https://codeforces.com/gym/607625/problem/C

from collections import defaultdict
t=int(input())

for _ in range(t):
    n=int(input())
    arr=list(map(int, input().split()))
        
    freq=defaultdict(int)
    max_freq=-1
    for num in arr:
        freq[num]+=1
    # print(freq)
    for key, val in freq.items():
        max_freq = max(max_freq, val)
    # print(max_freq)
    print(max(2*max_freq - n, n%2))

