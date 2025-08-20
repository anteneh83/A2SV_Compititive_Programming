# Problem: Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # nums=[]
        # while head:
        #     nums.append(head.val)
        #     head = head.next
        
        # nums.reverse()
        # # print(nums)
        # # print(head)
        # dummy = ListNode(0)
        # head = dummy

        # for num in nums:
        #     head.next = ListNode(num)
        #     head = head.next
        # return dummy.next
        prev= None
        next=None
        curr= head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr=next
        return prev
        