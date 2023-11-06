# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        
        # Iterative:
        prev, curr = None, head
        while curr != None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev

        # Recursive:
        # if head == None or head.next == None:
        #     return head

        # new = self.reverseList(head.next) # 5

        # head.next.next = head
        # head.next = None
        # return new