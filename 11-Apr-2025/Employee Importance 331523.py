# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        mp={e.id: e for e in employees}
        # print(mp)
        # def dfs(idx):
        #     emp=mp[idx]
        #     total=emp.importance

        #     for sub_id in emp.subordinates:
        #         total+=dfs(sub_id)
        #     return total

        # return dfs(id)

        stack=[id]
        total=0

        while stack:
            curr=stack.pop()
            emp=mp[curr]
            total+=emp.importance

            stack.extend(emp.subordinates)
        return total
