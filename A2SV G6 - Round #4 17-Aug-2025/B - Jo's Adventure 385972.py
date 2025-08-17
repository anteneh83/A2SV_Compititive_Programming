# Problem: B - Jo's Adventure - https://codeforces.com/gym/590053/problem/B

n, m = map(int, input().split())
height = list(map(int, input().split()))
# f_damage = [0]*(n)
# for i in range(1, n):
#     diff = height[i] - height[i-1]
#     if diff < 0:
#         f_damage[i] = f_damage[i-1] + abs(diff)

# b_damage=[0]*n
# for i in range(n-2, 0, -1):
#     diff = height[i] - height[i+1]
#     if diff < 0:
#         b_damage[i] = b_damage[i-1] + abs(diff)
# # print(b_damage)
# f_pref = [0]*n
# for i in range(1,n):
#     f_pref[i] = f_pref[i-1] + f_damage[i]
# b_damage.reverse()
# # print(b_damage)
# b_pref = [0]*n
# for i in range(1,n):
#     b_pref[i] = b_pref[i-1] + b_damage[i]
# # print(b_pref)
# for _ in range(m):
#     damage = 0
#     p, q = map(int, input().split())
#     if q > p:
#         print(f_pref[q-1] - f_pref[p-1])
#     else:
#         print(abs(b_pref[n-p] - b_pref[n-q]))

f= [0]*(n+1)
for i in range(1, n):
    f[i+1] = f[i] + max(0, height[i-1] - height[i])  
# print(f) 
b=[0]*(n+1)
for i in range(n-1, 0, -1):
    b[i] = b[i+1] + max(0, height[i] - height[i-1])
# print(b)

for _ in range(m):
    p, q = map(int, input().split())
    if q > p:
        print(f[q] - f[p])
    else:
        print(b[q] - b[p])