# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1; p2 = l2
        if p1 is None: return p2
        if p2 is None: return p1
        if l1.val > l2.val:
            root = l2
            p2 = l2.next
        else:
            root = l1
            p1 = l1.next
        curr = root
        while p1 and p2:
            if p1.val > p2.val:
                curr.next = p2
                p2 = p2.next
                curr = curr.next
            else:
                curr.next = p1
                p1 = p1.next
                curr = curr.next

        curr.next = p1 if p1 else p2
        return root