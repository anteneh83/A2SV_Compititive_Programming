# Problem: Partition Array According to Given Pivot - https://leetcode.com/problems/partition-array-according-to-given-pivot/description/

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lessThan=[]
        greaterThan=[]
        equal=[]
        for num in nums:
            if num < pivot:
                lessThan.append(num)
            elif num > pivot:
                greaterThan.append(num)
            else:
                equal.append(num)
        return lessThan + equal  + greaterThan