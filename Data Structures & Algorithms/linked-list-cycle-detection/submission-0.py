# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        try:
            f, s = head, head
            while True:
                f = f.next.next
                s = s.next

                print("")

                if s.val == f.val:
                    return True

        #hit none
        except:
            return False