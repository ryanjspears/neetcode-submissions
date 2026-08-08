# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        final = ListNode(0)
        p = final
        carry = 0
        while l1 is not None or l2 is not None:
            print("hit")
            v1 = l1.val if l1 is not None else 0
            v2 = l2.val if l2 is not None else 0
            tmp = v1 + v2 + carry
            if tmp >= 10:
                tmp %= 10
                carry = 1
            else:
                carry = 0

            p.next = ListNode(tmp)
            print(p.val)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            p = p.next

        #one more 
        if carry > 0:
            p.next = ListNode(carry)

        return final.next


