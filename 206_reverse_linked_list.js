/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */

// Input:
// 1 -> 2 -> 3 -> null

// Output:
// 3 -> 2 -> 1 -> null

var reverseList = function (head) {
  let prev = null;

  while (head !== null) {

    // Capture next node
    let next = head.next;
    // 1:   next = 1.next = 2
    // 2:   next = 2.next = 3
    // 3:   next = 3.next = null

    // Re assign Next node to Previous node
    head.next = prev;
    // 1:   1.next -> null
    // 2:   2.next -> 1
    // 3:   3.next -> 2

    // Re assign Previous node to Head
    prev = head;
    // 1:   prev = 1
    // 2:   prev = 2
    // 3:   prev = 3

    // Re assign Head to Next
    head = next;
    // 1:   head = 2
    // 2:   head = 3
    // 3:   head = null
  }

  return prev;
};