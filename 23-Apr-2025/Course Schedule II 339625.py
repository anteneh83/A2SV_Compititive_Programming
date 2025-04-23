# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree=[0]*numCourses
        graph=[[] for _ in range(numCourses)]
        for u, v in prerequisites:
            indegree[u]+=1
            graph[v].append(u)
        # print(indegree)
        # print(graph)
        ans=[]
        que=deque()
        for i in range(len(indegree)):
            if indegree[i]==0:
                que.append(i)
        # print(que)

        while que:
            num=que.popleft()
            ans.append(num)

            for val in graph[num]:
                indegree[val]-=1
                if indegree[val]==0:
                    que.append(val)
        if len(ans)==numCourses:
            return ans
        return []

        
