# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        visited = set()

        while headA:
            if headA not in visited:
                visited.add(headA)
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