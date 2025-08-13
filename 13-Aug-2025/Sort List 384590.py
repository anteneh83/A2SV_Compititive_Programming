# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def split(head):
            slow=fast=head
            while fast and fast.next:
                fast = fast.next.next
                if fast:
                    slow = slow.next
            second = slow.next
            slow.next=None
            return second

        def merge(first, second):
            if not first:
                return second
            if not second:
                return first
            
            if first.val < second.val:
                first.next = merge(first.next, second)
                return first
            else:
                second.next = merge(first, second.next)
                return second

        def mergeSort(head):
            if not head or not head.next:
                return head
            
            second = split(head)
            head = mergeSort(head)
            second = mergeSort(second)

            return merge(head, second)
        return mergeSort(head)
        
        