# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        ### 1. Using a set
        # Time: O(n)
        # Space: O(n)

        # visited_nodes = set()
        # while head:
        #     if head not in visited_nodes:
        #         visited_nodes.add(head)
        #     else:
        #         return True
        #     head = head.next
        # return False

        ### 2. Two pointers
        # - They move at different speeds. If there is a cycle the fast pointer will 
        # eventually catch up to the slow pointer
        # Time: O(n)
        # Space: O(1)


        fast_pointer = head
        while fast_pointer and fast_pointer.next:
            head = head.next
            fast_pointer = fast_pointer.next.next
            if head == fast_pointer:
                return True
        
        return False


        # [3,2,0,-4],

        # 3 -> 2 -> 0 -> -4 -> 2 -> 0 -> -4 -> 2