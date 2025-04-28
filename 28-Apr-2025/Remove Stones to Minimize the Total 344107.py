# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap=[]
        for pile in piles:
            heapq.heappush(heap, -pile)
        # print(heap) 
        for i in range(k):
            top=-heapq.heappop(heap)
            val=top - top//2
            heapq.heappush(heap, -val)
        return -sum(heap)

        