# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

t = int(input())
for _ in range(t):
    x = int(input())
    
    low  = x & -x

    if x ^ low !=0 :
        print(low)
    else:
        if x==1:
            print(3)
        else:
            print(x + 1)