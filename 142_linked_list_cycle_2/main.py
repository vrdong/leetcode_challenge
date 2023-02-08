from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Tags = [two pointers]
        Using fast and slow to detect circle in linked list
        '''
        if not head:
            return None

        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                start = head
                return self.findCyclePoint(start, slow)

        return None

    def findCyclePoint(self, first_slow: Optional[ListNode], second_slow: Optional[ListNode]) -> Optional[ListNode]:
        '''
        fast move double step of slow
        If fast move slow's steps more -> meet slow again
        If a pointer move from head with slow's steps. Fast and new point wil meet at circle points
        '''
        while first_slow != second_slow:
            first_slow = first_slow.next
            second_slow = second_slow.next
        return first_slow
