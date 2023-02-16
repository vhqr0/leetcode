from typing import Optional, List


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeKLists(self,
                    lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]

        if len(lists) > 2:
            m = len(lists) // 2
            l1, l2 = lists[:m], lists[m:]
            return self.mergeKLists([
                self.mergeKLists(l1),
                self.mergeKLists(l2),
            ])

        list1, list2 = lists[0], lists[1]

        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val < list2.val:
            h = list1
            list1 = list1.next
        else:
            h = list2
            list2 = list2.next

        t = h

        while list1 is not None or list2 is not None:
            if list1 is None:
                t.next = list2
                break
            if list2 is None:
                t.next = list1
                break

            if list1.val < list2.val:
                t.next = list1
                t = t.next
                list1 = list1.next
            else:
                t.next = list2
                t = t.next
                list2 = list2.next

        return h
