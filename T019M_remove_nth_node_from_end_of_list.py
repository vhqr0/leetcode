from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def removeNthFromEnd(self, head: Optional[ListNode],
                         n: int) -> Optional[ListNode]:
        t = head
        for _ in range(n - 1):
            if t.next is None:
                return None
            t = t.next

        if t.next is None:  # head is the nth node
            return head.next

        h, t = head, t.next
        while t.next is not None:
            h, t = h.next, t.next

        h.next = h.next.next

        return head
