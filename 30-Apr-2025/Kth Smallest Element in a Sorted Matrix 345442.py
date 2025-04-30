# Problem: Kth Smallest Element in a Sorted Matrix - https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        hp=[]
        heapify(hp)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heapq.heappush(hp, matrix[i][j])
        # print(hp)
        for _ in range(1, k):
            heapq.heappop(hp)
        # print(hp)
        return hp[0]