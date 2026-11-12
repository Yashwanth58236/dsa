

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        phA = headA
        phB = headB

        while phA != phB:
             if phA is None:
                     phA = headB
             else:
                    phA = phA.next
             if phB is None:
                  phB = headA
             else:
                   phB = phB.next

        return phA