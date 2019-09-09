# 21. Merge Two Sorted Lists

# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

def mergeLists(self, l1, l2):
  # check for empty edge cases
  if l1 is None and l2 is None:
    return None
  elif l1 is None and l2 is not None:
    return l2
  elif l2 is None and l1 is not None:
    return l1
  
  # decide which linked list to splice into
  if l1.val < l2.val:
    insert = l1
    remove = l2
  else:
    insert = l2
    remove = l1
  
  # create list to return
  result = insert
  while remove is not None:
    if insert.next is None:
      insert.next = remove
      return result
    elif remove.val <= insert.next.val:
      # save the original 'next values'
      insert_pointer = insert.next
      remove_pointer = remove.next

      # insert l2 into l1 between two nodes
      insert.next = remove
      remove.next = insert_pointer
      remove = remove_pointer

      # move onto the next values to check in the linked lists
  insert = insert.next
  return result
