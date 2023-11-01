# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        visited = set()

        ### 1. 
        # while headA:
        #     if headA not in visited:
        #         visited.add(headA)
        #     headA = headA.next

        # while headB:
        #     if headB not in visited:
        #         visited.add(headB)
        #     else:
        #         return headB
        #     headB = headB.next

        # return None

        while headA and headB:
            if headA not in visited:
                visited.add(headA)
            else:
                return headA
            if headB not in visited:
                visited.add(headB)
            else: 
                return headB
            headA = headA.next
            headB = headB.next

        print(headA)
        print(headB)

        while headA:
            if headA not in visited:
                visited.add(headA)
            else:
                return headA
            headA = headA.next

        while headB:
            if headB not in visited:
                visited.add(headB)
            else:
                return headB
            headB = headB.next

        return None

        

        # listA = [4,1,8,4,5], 
        # listB = [5,6,1,8,4,5]