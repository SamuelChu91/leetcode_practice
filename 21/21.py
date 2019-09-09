# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
  def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    sentinel = ListNode(None)
    current = sentinel
    
    while l1 is not None and l2 is not None:
      if l1.val < l2.val:
        current.next = l1
        l1 = l1.next
      else:
        current.next = l2
        l2 = l2.next
      current = current.next
        
    if l1 is None:
      current.next = l2
    else:
      current.next = l1
    
    return sentinel.next
