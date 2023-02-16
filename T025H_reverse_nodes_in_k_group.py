from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseKGroup(self, head: Optional[ListNode],
                      k: int) -> Optional[ListNode]:
        t = head
        for _ in range(k - 1):
            if t is None:
                return head
            t = t.next

        # reverse before hold left nodes
        if t is None:
            return head
        t.next = self.reverseKGroup(t.next, k)
        t = t.next

        for _ in range(k):
            h, head = head, head.next
            h.next = t
            t = h

        return t
