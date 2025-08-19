# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_hp=[]
        for i in range(len(lists)):
            node=lists[i]
            while node:
                heapq.heappush(min_hp, node.val)
                node=node.next
        # print(min_hp)
        n=len(min_hp)
        sorted_list=[]
        for _ in range(n):
            sorted_list.append(heappop(min_hp))
        # print(sorted_list)
        dummy=ListNode(0)
        curr=dummy
        for num in sorted_list:
            curr.next=ListNode(num)
            curr=curr.next
        return dummy.next
