# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            digits1 = l1.val if l1 is not None else 0
            digits2 = l2.val if l2 is not None else 0

            sum_val = digits1 + digits2 + carry
            if sum_val >= 10:
                carry = 1
                sum_val -= 10
            else:
                carry = 0

            tail.next = ListNode(sum_val)
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
                
        result = dummyHead.next
        dummyHead.next = None
        return result



        # Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
        # Output: [8,9,9,9,0,0,0,1]

        # 9999 + 9999999 = 10009998