from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]):
    cur = list3 = ListNode()
    while list1 and list2:               
        if list1.val < list2.val:
            cur.next = list1
            list1, cur = list1.next, list1
        else:
            cur.next = list2
            list2, cur = list2.next, list2
            
    if list1 or list2:
        cur.next = list1 if list1 else list2
        
    return list3.next