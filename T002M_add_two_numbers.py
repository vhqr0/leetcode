from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode],
                      l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        l1.val += l2.val
        if l1.val >= 10:
            l1.val -= 10
            if l1.next is None:
                l1.next = ListNode(val=1)
            else:
                l1.next.val += 1
                if l2.next is None:  # force check: l1.next.val >= 10
                    l2.next = ListNode()

        l1.next = self.addTwoNumbers(l1.next, l2.next)
        return l1
