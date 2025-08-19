# Problem: C - Binary Flip - https://codeforces.com/gym/590053/problem/C

t = int(input())

for _ in range(t):
    n = int(input())
    given = list(input().strip())
    req = list(input().strip())
    
    prefix_zeros=[0]*n
    prefix_ones=[0]*n

    if given[0]=='0':
        prefix_zeros[0]=1
    else:
        prefix_ones[0]=1
    
    for i in range(1, n):
        prefix_zeros[i] = prefix_zeros[i-1] + (given[i] == '0')
        prefix_ones[i] = prefix_ones[i-1] + (given[i] == '1')

    flag = True
    flip=False
    for i in range(n-1, -1, -1 ):
        if flip:
            given[i] = '0' if given[i]=='1' else '1'
        if given[i] != req[i]:
            if prefix_ones[i] == prefix_zeros[i]:
                flip=not flip
            else:
                flag = False
                break
    print('YES' if flag else 'NO')

            
  
