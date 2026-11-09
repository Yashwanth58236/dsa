# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
       pre=None
       cur=head
       while cur:
          next=cur.next
          cur.next=pre
          pre=cur
          cur=next
       return pre