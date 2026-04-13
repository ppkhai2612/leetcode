# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() # linked list is returned as a sum
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            # If l1 or l2 is not empty, return the value; otherwise, return 0
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            carry, sum_val = divmod(v1 + v2 + carry, 10)

            # points to the sum value that was just calculated
            curr.next = ListNode(sum_val) # 
            
            # update pointers
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next