'''
Add Two Number
https://leetcode.com/problems/add-two-numbers/
Description
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.


Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''



from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    
    # Myself
    def addTwoNumbersMyself(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Space complexity: O(m+n)
        Time complexity: O(m+n)
        '''
        head = cur_node = ListNode(0, None)
        head1 = l1
        head2 = l2
        
        redundant = 0
        while head1 or head2:
            if head1:
                val1  = head1.val
                head1 = head1.next
            else:
                val1 = 0
                
            if head2:
                val2 = head2.val
                head2 = head2.next
            else:
                val2 = 0
            
            cur_val = val1 + val2 + redundant
            if cur_val >= 10:
                cur_val = cur_val % 10
                redundant = 1
            else:
                redundant = 0
                
            cur_node.next = ListNode(cur_val, None)
            cur_node = cur_node.next
        
        if redundant == 1:
            cur_node.next = ListNode(1, None)
        return head.next
        
    # optimal solution same as mine but more clear
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        cur = dummyHead
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            
            column_sum =l1_val + l2_val + carry
            carry = column_sum // 10
            new_node = ListNode(column_sum % 10)
            cur.next = new_node
            cur = cur.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
           
        
        return dummyHead.next
             
            
    
    
            
                
        