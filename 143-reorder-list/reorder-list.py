
class Solution(object):
    def reorderList(self, head):

        # Step 1: Find the middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half
        cur = slow.next
        slow.next = None
        prev = None

        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        # Step 3: Merge both halves
        first = head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
