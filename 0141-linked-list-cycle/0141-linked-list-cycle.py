# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        values = set()
        while head:
            if head not in values:
                values.add(head)
            else:
                return True
            head = head.next
        return False


        # [3,2,0,-4],

        # 3 -> 2 -> 0 -> -4 -> 2 -> 0 -> -4 -> 2