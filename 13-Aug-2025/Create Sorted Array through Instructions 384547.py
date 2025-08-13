# Problem: Create Sorted Array through Instructions - https://leetcode.com/problems/create-sorted-array-through-instructions/

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        nums=[]
        cost=0
        for num in instructions:
            less = bisect.bisect_left(nums, num)
            greater = bisect.bisect_right(nums, num)
            cost += min(less, len(nums)-greater)
            bisect.insort(nums, num)
        return cost%(10**9 + 7)