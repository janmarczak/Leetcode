# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head == None:
            return False

        values = set()

        while head.next:
            if head not in values:
                values.add(head)
            else:
                return True
            head = head.next

        return False


        