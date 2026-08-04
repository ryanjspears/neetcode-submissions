# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return
        if head.next is None:
            return

        i = -1
        dummy = ListNode(val=0, next=head)
        lag = dummy
        while lag.next is not None:
            i+=1
            if i%2 == 1:
                tmp = lag # before
                snip = tmp.next # after
                # go to end, snip, and insert

                #go to end
                while snip.next is not None:
                    tmp = snip
                    snip = snip.next
                
                #at end and snip
                tmp.next = None

                #insert at main pointer
                tmp = lag
                tmp = tmp.next

                lag.next = snip
                snip.next = tmp

            lag = lag.next







        