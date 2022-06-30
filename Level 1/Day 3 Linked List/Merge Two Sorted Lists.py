# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = None
        if list1 is None and list2 is None:
            return 
        elif list1 is None and list2 is not None:
            temp = list2
            list2 = list2.next
        elif list1 is not None and list2 is None:
            temp = list1
            list1 = list1.next
        elif list1.val < list2.val:
            temp = list1
            list1 = list1.next
        else:
            temp = list2
            list2 = list2.next
        rt = temp
        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        if list1:
            temp.next = list1
            list1 = list1.next
            temp = temp.next
        elif list2:
            temp.next = list2
            list2 = list2.next
            temp = temp.next
        return rt


# Alternate Solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        rt = ListNode(1)
        temp = rt
        rt = temp
        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        if list1:
            temp.next = list1
            list1 = list1.next
            temp = temp.next
        elif list2:
            temp.next = list2
            list2 = list2.next
            temp = temp.next
        return rt.next  