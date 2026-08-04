# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def clean(self, lists):
        removed=0
        for i in range(len(lists)):
            if lists[i-removed] is None:
                lists.pop(i-removed)
                removed+=1

    def popFront(self, node):
        return node.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        self.clean(lists)
        # find min= 1
        final = ListNode(0)
        p = final

        #while lists are full
        mini = None
        while len(lists) > 0:
            print(f"mini: {mini}")
            #clean lists from Nones
            changed = False
            self.clean(lists)

            #for each node in list find the min
            if not mini:

                for node in lists:
                    print(f"mini_inner: {mini}")
                    if mini is None:
                        mini = node.val
                    else:
                        if mini > node.val:
                            mini = node.val
            
            #min found or still pruning
            #iterate over lists again and front pop and add to final
            i = -1
            for node in lists:
                i +=1
                if node.val == mini:
                    p.next = ListNode(node.val)
                    p = p.next
                    lists[i] = self.popFront(node)
                    changed = True

            #if not chnaged then mini is axuaghted
            if not changed:
                mini = None


        
        return final.next



    # #iterate over 0th index and get min

    # #make a new empty linked like

    # #now iterate over each list and pop the front if that min is present

    # keep passing until now more pops