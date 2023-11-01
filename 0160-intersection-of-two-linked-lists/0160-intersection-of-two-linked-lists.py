# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        ### 1. Using a set
        # Time: O(n+m)
        # Space: O(n+m)

        # visited = set()
        # while headA and headB:
        #     if headA not in visited:
        #         visited.add(headA)
        #     else:
        #         return headA
        #     if headB not in visited:
        #         visited.add(headB)
        #     else: 
        #         return headB
        #     headA = headA.next
        #     headB = headB.next

        # while headA:
        #     if headA not in visited:
        #         visited.add(headA)
        #     else:
        #         return headA
        #     headA = headA.next

        # while headB:
        #     if headB not in visited:
        #         visited.add(headB)
        #     else:
        #         return headB
        #     headB = headB.next

        # return None

        ### 2. Lenghts
        # Two variables storing the lenghts of the linked lists

        c1 = c2 = 0
        temp1, temp2 = headA, headB

        # Get the length
        while temp1 or temp2:
            if temp1:
                c1 += 1
                temp1 = temp1.next
            if temp2:
                c2 += 1
                temp2 = temp2.next

        diff = c1 - c2
        if diff < 0: # headB is bigger than headA by diff
            while diff != 0:
                headB = headB.next
                diff += 1
        else: # headA is bigger than headB by diff
            while diff != 0:
                headA = headA.next
                diff -= 1

        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None