# Problem: Kth Largest Element in an Array - https://leetcode.com/problems/kth-largest-element-in-an-array/description/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap=[]
        for num in nums:
            heapq.heappush(max_heap, -num)
        # print(max_heap)
        for i in range(k-1):
            heapq.heappop(max_heap)
            # print(max_heap)
        return -max_heap[0]