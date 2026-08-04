# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None


        #get length
        length = 0
        p = head
        while p is not None:
            length+=1
            p = p.next

        i = -1
        dummy = ListNode(val=0, next=head)
        lag = dummy
        t = length - n
        while lag.next is not None:
            print(f"val= {lag.val}, is none{lag.next is None}")
            i+=1
            if i == t:
                #snip at n
                snip = lag.next # after
                nexty = snip.next
                lag.next = nexty
                return dummy.next
            lag = lag.next


        return dummy.next
