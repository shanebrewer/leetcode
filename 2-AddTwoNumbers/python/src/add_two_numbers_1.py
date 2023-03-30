# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        maxLength = 0
        result = []
        
        # if len(l1) > len(l2):
        #     maxLength = len(l2)
        # elif len(l2) < len(l1):
        #     maxLength = len(l1)
        # else:
        #     maxLength = len(l1)
            
        carry = 0
        
        for (a, b, c) in zip(l1, l2):
            
        
        return result                
