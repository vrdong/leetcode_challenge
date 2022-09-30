'''
19. Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
 
Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head 
        num_node = 0
        while current != None:
            num_node += 1
            current = current.next
        
        del_idx_node = num_node - n + 1
        
        current, before = head, head
        count = 0
        
        while current != None:
            count += 1
            if count == del_idx_node:
                if count == 1:
                    head = head.next
                else:
                    before.next = current.next
            before = current 
            current = current.next
         
         
         
    # Better solution
    # Using 2 pointer 
    # A fast pointer go a head n node slow pointer
    # If fast pointer reach to the end of linked list => slow point reach to the n-th from the end of list
    # TODO implement better solution
    