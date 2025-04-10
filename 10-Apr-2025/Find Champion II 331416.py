# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree=[0]*n

        for u, v in edges:
            indegree[v]+=1
        # print(indegree)
        champion=[i for i in range(n) if indegree[i]==0]
        # print(champion)
        if len(champion)==1: return champion[0]
        return -1