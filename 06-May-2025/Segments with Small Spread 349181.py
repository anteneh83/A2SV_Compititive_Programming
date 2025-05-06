# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

from collections import deque
n, s = map(int, input().split())  
nums = list(map(int, input().split()))  

# window = SortedList()
min_que= deque()
max_que = deque()  
left = 0
ans = 0

for right in range(len(nums)):

    while min_que and nums[min_que[-1]] >= nums[right]:
        min_que.pop()  
    min_que.append(right)

    while max_que and nums[max_que[-1]] <= nums[right]:
        max_que.pop()
    max_que.append(right)
    
    while nums[max_que[0]] - nums[min_que[0]] > s:
        if min_que[0] == left:
            min_que.popleft()
        if max_que[0] == left:
            max_que.popleft()
        left+=1
        
    ans += (right - left + 1)  

print(ans)
