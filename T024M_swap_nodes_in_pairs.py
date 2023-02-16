from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        second = head.next
        head.next, second.next = second.next, head

        head, second = second, head

        second.next = self.swapPairs(second.next)

        return head
