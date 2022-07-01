# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        while head:
            if head.val == '_':
                return head
            head.val = '_'
            head = head.next
        return 
        
#ALTERNATE SOLUTION

        f, s = head, head
        while f and f.next:
            f = f.next.next
            s = s.next
            if f == s:
                s = head
                while f != s:
                    s = s.nexts
                    f = f.next
                return s
        return 