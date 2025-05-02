# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        arrenged_tasks = [(et, pt, i) for i, (et, pt) in enumerate(tasks)]
        arrenged_tasks.sort()
        # print(arrenged_tasks)
        ans=[]
        min_hp=[]
        time=i=0
        n=len(arrenged_tasks)

        while i < n or min_hp:
            # add to available tasks
            while i < n and arrenged_tasks[i][0] <= time:
                et, pt, idx = arrenged_tasks[i]
                heappush(min_hp, (pt, idx))
                i+=1
            # check the cpu have tasks or idle
            if min_hp:
                pt, idx = heappop(min_hp)
                ans.append(idx)
                time+=pt
            else:
                time = arrenged_tasks[i][0]
        return ans
            
            

